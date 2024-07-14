from claid.dispatch.proto.claidservice_pb2 import CLAIDConfig, ModuleAnnotation, DataPackage
import json
from google.protobuf.json_format import Parse, ParseDict, MessageToJson

class CLAID:

    def __init__(self):
        pass

    def __make_input_channel(self, channel_name: str, module_name: str):
        package = DataPackage()
        package.channel = channel_name
        package.target_module = module_name

        return package

    def __make_output_channel(self, channel_name: str, module_name: str):
        package = DataPackage()
        package.channel = channel_name
        package.source_module = module_name

        return package


    def get_available_modules(self):
        modules = dict()

        module_description = ModuleAnnotation()
        module_description.module_description = "This is a Module that allows to record audio data from the Microphone"
        module_description.properties.append("RecordingMode")
        module_description.properties.append("BitRate")
        module_description.properties.append("SamplingRate")

        module_description.property_descriptions.append("Mode for recording data, one of: [Continuous, Chunks]")
        module_description.property_descriptions.append("Bitrate of the audio sample, one of [8, 16, 32]")
        module_description.property_descriptions.append("Sampling Rate, e.g. 44100")
        module_description.channel_definition.append(self.__make_output_channel("AudioDataChannel", "AudioRecorder"))
        module_description.channel_description.append("Channel where the recorded AudioData will be posted to.")
        
        modules["AudioRecorder"] = module_description

        module_description = ModuleAnnotation()
        module_description.module_description = "This is a Module that allows to record data from any channel and stores incoming data on the filesystem"
        module_description.properties.append("fileFormat")
        module_description.properties.append("fileName")
        module_description.properties.append("storagePath")

        module_description.property_descriptions.append("Format/codec for the file. One of [JSON, BINARY, BatchJSON, BatchBBINARY]")
        module_description.property_descriptions.append("Naming convention for the files to store. Can use strftime specifiers, e.g.: my_file\%H_\%M")
        module_description.property_descriptions.append("Storage path for the files, e.g. /sdcard/MyFiles")
        module_description.channel_definition.append(self.__make_input_channel("DataChannel", "DataSaver"))
        module_description.channel_description.append("Channel with incoming data.")
        
        modules["DataSaver"] = module_description

        image_processor_description = ModuleAnnotation()
        image_processor_description.module_description = "Processes images by applying filters and transformations."
        image_processor_description.properties.append("filterType")
        image_processor_description.properties.append("resizeFactor")
        image_processor_description.properties.append("outputFormat")

        image_processor_description.property_descriptions.append("Type of filter to apply, e.g., [Blur, Sharpen, Grayscale].")
        image_processor_description.property_descriptions.append("Factor by which to resize the image, e.g., 0.5 for half the size.")
        image_processor_description.property_descriptions.append("Output format for processed images, e.g., [JPEG, PNG].")
        image_processor_description.channel_definition.append(self.__make_input_channel("InputImages", "ImageProcessor"))
        image_processor_description.channel_description.append("Input channel for images to be processed.")
        image_processor_description.channel_definition.append(self.__make_output_channel("ProcessedImages", "ImageProcessor"))
        image_processor_description.channel_description.append("Output channel for processed images.")

        modules["ImageProcessor"] = image_processor_description

        # Add DataAnalyzer Module
        data_analyzer_description = ModuleAnnotation()
        data_analyzer_description.module_description = "Analyzes incoming data and extracts key insights or statistics."
        data_analyzer_description.properties.append("analysisType")
        data_analyzer_description.properties.append("threshold")
        data_analyzer_description.properties.append("outputMetrics")

        data_analyzer_description.property_descriptions.append("Type of analysis to perform, e.g., [Descriptive, Predictive, Diagnostic].")
        data_analyzer_description.property_descriptions.append("Threshold value for specific analyses.")
        data_analyzer_description.property_descriptions.append("List of specific metrics to output.")
        data_analyzer_description.channel_definition.append(self.__make_input_channel("InputData", "DataAnalyzer"))
        data_analyzer_description.channel_description.append("Input channel for data to be analyzed.")
        data_analyzer_description.channel_definition.append(self.__make_output_channel("AnalyzedResults", "DataAnalyzer"))
        data_analyzer_description.channel_description.append("Output channel for analyzed results.")

        modules["DataAnalyzer"] = data_analyzer_description

        # Add ParallelProcessor Module
        parallel_processor_description = ModuleAnnotation()
        parallel_processor_description.module_description = "Processes data in parallel with multiple input and output channels."
        parallel_processor_description.channel_definition.append(self.__make_input_channel("InputData1", "ParallelProcessor"))
        parallel_processor_description.channel_description.append("First input channel for parallel processing.")
        parallel_processor_description.channel_definition.append(self.__make_input_channel("InputData2", "ParallelProcessor"))
        parallel_processor_description.channel_description.append("Second input channel for parallel processing.")
        parallel_processor_description.channel_definition.append(self.__make_output_channel("OutputData1", "ParallelProcessor"))
        parallel_processor_description.channel_description.append("First output channel for parallel processing.")
        parallel_processor_description.channel_definition.append(self.__make_output_channel("OutputData2", "ParallelProcessor"))
        parallel_processor_description.channel_description.append("Second output channel for parallel processing.")

        modules["ParallelProcessor"] = parallel_processor_description

        # Add DataTransformer Module
        data_transformer_description = ModuleAnnotation()
        data_transformer_description.module_description = "Transforms data with multiple input and output channels."
        data_transformer_description.channel_definition.append(self.__make_input_channel("InputData", "DataTransformer"))
        data_transformer_description.channel_description.append("Input channel for data transformation.")
        data_transformer_description.channel_definition.append(self.__make_output_channel("OutputData1", "DataTransformer"))
        data_transformer_description.channel_description.append("First output channel for data transformation.")
        data_transformer_description.channel_definition.append(self.__make_output_channel("OutputData2", "DataTransformer"))
        data_transformer_description.channel_description.append("Second output channel for data transformation.")

        modules["DataTransformer"] = data_transformer_description

        accelerometer_collector_description = ModuleAnnotation()
        accelerometer_collector_description.module_description = "Collects accelerometer data from a device sensor."
        accelerometer_collector_description.properties.append("samplingRate")
        accelerometer_collector_description.properties.append("collectionDuration")

        accelerometer_collector_description.property_descriptions.append("Sampling rate for accelerometer data, e.g., 50 Hz.")
        accelerometer_collector_description.property_descriptions.append("Duration for data collection in seconds.")
        accelerometer_collector_description.channel_definition.append(self.__make_output_channel("AccelerometerData", "AccelerometerCollector"))
        accelerometer_collector_description.channel_description.append("Output channel for collected accelerometer data.")

        modules["AccelerometerCollector"] = accelerometer_collector_description

        return modules
    
    def get_input_channels_of_module(self, module_annotation: ModuleAnnotation):
        channels = list()
        for channel in module_annotation.channel_definition:
            if channel.target_module != "":
                channels.append(channel.channel)

        return channels
    
    

    def get_output_channels_of_module(self, module_annotation: ModuleAnnotation):
        channels = list()
        for channel in module_annotation.channel_definition:
            if channel.source_module != "":
                channels.append(channel.channel)

        return channels

    def save_config_to_file(self, config, json_file_path):
        # Use the .to_dict() method to convert the protobuf message to a dictionary
        json_data = MessageToJson(config, including_default_value_fields=True, preserving_proto_field_name=True)
        print(json_data)
        with open(json_file_path, 'w') as f:
            f.write(json_data)

# message ModuleAnnotation
# {
# string module_description  = 1;
# repeated string properties = 2;
# repeated string property_descriptions = 3;
# repeated DataPackage channel_definition = 4;
# repeated string channel_description = 5;
# }