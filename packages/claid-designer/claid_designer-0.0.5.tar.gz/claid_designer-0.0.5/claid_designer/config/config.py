from claid.dispatch.proto.claidservice_pb2  import CLAIDConfig, ModuleAnnotation, DataPackage
from google.protobuf.json_format import Parse, ParseDict, MessageToJson
import json
from config.channel_description import ChannelDescription

class Config():

    def __init__(self):
        self.config = None

    def load_config_from_file(self, json_file_path):
        self.config = CLAIDConfig()
        with open(json_file_path, 'r') as f:
            json_data = json.load(f)
            # Use ParseDict to populate the protobuf message from a dictionary
            ParseDict(json_data, self.config)
        return self.config

    def save_config_to_file(self, path):
        Config.save_config_to_file(self.config, path)

    #TODO: Static methods, etc. recherchieren
    @staticmethod
    def save_config_to_file(config, json_file_path):
        # Use the .to_dict() method to convert the protobuf message to a dictionary
        json_data = MessageToJson(config, including_default_value_fields=True, preserving_proto_field_name=True)
        with open(json_file_path, 'w') as f:
            f.write(json_data)

    def get_config_data(self):
        return self.config
    
    def get_channel_descriptions(self):
        descriptions = dict()

        for host in self.config.hosts:
            for module in host.modules:
                input_channels = module.input_channels
                output_channels = module.output_channels

                for input_channel_name in input_channels:
                    input_channel_connection = input_channels[input_channel_name]

                    if not input_channel_connection in descriptions:
                        descriptions[input_channel_connection] = ChannelDescription(input_channel_connection, list(), list())

                    descriptions[input_channel_connection].subscriber_modules.append((host.hostname, module.id, input_channel_name))

                for output_channel_name in output_channels:
                    output_channel_connection = output_channels[output_channel_name]

                    if not output_channel_connection in descriptions:
                        descriptions[output_channel_connection] = ChannelDescription(output_channel_connection, list(), list())

                    descriptions[output_channel_connection].publisher_modules.append((host.hostname, module.id, output_channel_name))

        return descriptions



