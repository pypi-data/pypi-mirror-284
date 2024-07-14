import sys
from PyQt5.QtWidgets import QTabWidget, QLabel, QHeaderView, QFrame, QTableWidget, QTableWidgetItem, QWidget, QGraphicsWidget, QMessageBox, QErrorMessage, QInputDialog, QLineEdit, QApplication, QGraphicsScene, QGraphicsView, QGraphicsProxyWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QGraphicsRectItem, QGraphicsLineItem, QDialog, QSizePolicy, QListWidget, QPushButton
from PyQt5.QtCore import QPointF, Qt, QLineF, QSize, QRectF, pyqtSignal
from PyQt5.QtGui import QResizeEvent, QFontMetrics
from ui.module_graphics_item import ModuleGraphicsItem

from ui.non_scrollable_graphics_view import NonScrollableGraphicsView

from claid import CLAID
from claid.dispatch.proto.claidservice_pb2  import CLAIDConfig, ModuleAnnotation, DataPackage

from ui.property_input_dialog import PropertyInputDialog

class ModuleCatalog(QWidget):

    on_catalog_closed = pyqtSignal()

    def __init__(self, parent_host, claid, host_name, module_injections_supported=False):

        super().__init__()

        self.parent_host = parent_host
        self.module_injections_supported = module_injections_supported
        self.claid = claid


        self.available_modules = self.claid.get_available_modules_for_host(host_name)
        if self.available_modules == None:
            self.close_catalog()
            return
        self.available_modules = dict(sorted(self.available_modules.items()))
        # Set up the main layout
        main_layout = QVBoxLayout(self)

        # Create a QGraphicsView and QGraphicsScene
        self.graphics_view = NonScrollableGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.scene)

        # Dimensions
        initial_width = 600
        initial_height = 600
        
        
        self.ratio_module_text = 0.3

        self.module_width = initial_width/4
        self.module_height = self.module_width * 2/3

        # Create a rectangle above the text
        self.rect_item = ModuleGraphicsItem("Test", "Test", 0, 0, self.module_width, self.module_height, [], [], [], [], [], [], [], movable=False)
        #! Should we delete the setPos code of as it is set in ResizeEvent() anyways?
        self.rect_item.setPos(initial_width//2 - self.module_width//2, (initial_height * self.ratio_module_text)//2 - self.module_height//2)
        self.scene.addItem(self.rect_item)

        # Create a horizontal line to separate text and rectangle
        #! Should we delete the arguments of QGraphicsLineItem as they are set in ResizeEvent() anyways?
        self.line_item = QGraphicsLineItem(0, initial_height * self.ratio_module_text, initial_width, initial_height * self.ratio_module_text)
        self.scene.addItem(self.line_item)

        # Create a QTextEdit with non-editable text
        self.module_text = QTextEdit()
        self.module_text.setPlainText("Empty")
        self.module_text.setReadOnly(True)
        self.module_text.setFrameShape(QTextEdit.NoFrame)
        self.module_text.setStyleSheet("border: none;")
        self.module_text.setFixedHeight(self.calculate_text_height("Empty"))
        # self.module_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Create a QGraphicsProxyWidget to embed the QTextEdit in the QGraphicsScene

        proxy_widget_inner = QWidget()
        proxy_widget_inner.setLayout(QVBoxLayout())
        proxy_widget_inner.layout().addWidget(self.module_text)
        self.proxy_widget = self.scene.addWidget(proxy_widget_inner)
        proxy_widget_inner.setStyleSheet("border: none;")

        proxy_widget_inner.layout().setSpacing(20)
        proxy_widget_inner.layout().setContentsMargins (0, 0, 0, 0)
        proxy_widget_inner.setStyleSheet("border: 0px")

        proxy_widget_inner.layout().addWidget(QLabel("Properties"))


        self.properties_table = QTableWidget()
        # Add necessary initialization for the first table
        self.properties_table.setRowCount(2)
        self.properties_table.setColumnCount(2)
        for i in range(2):
            for j in range(2):
                item = QTableWidgetItem(f"properties_table Item {i}, {j}")
                self.properties_table.setItem(i, j, item)

        # Hide grid lines
        self.properties_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.properties_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        # Remove frame
        self.properties_table.setFrameStyle(QFrame.NoFrame)
        self.properties_table.setWordWrap(True)
        proxy_widget_inner.layout().addWidget(self.properties_table)
        self.properties_table.horizontalHeader().sectionResized.connect(self.properties_table.resizeRowsToContents)

        proxy_widget_inner.layout().addWidget(QLabel("Channels"))
        self.channels_table = QTableWidget()
        # Add necessary initialization for the first table
        self.channels_table.setRowCount(2)
        self.channels_table.setColumnCount(2)
        for i in range(2):
            for j in range(2):
                item = QTableWidgetItem(f"channels_table Item {i}, {j}")
                self.channels_table.setItem(i, j, item)

        # Hide grid lines
        
        # Remove frame
        self.channels_table.setFrameStyle(QFrame.NoFrame)
        self.channels_table.setWordWrap(True)
        self.channels_table.horizontalHeader().sectionResized.connect(self.channels_table.resizeRowsToContents)
        proxy_widget_inner.layout().addWidget(self.channels_table)

        # Add the QGraphicsView to the main layout
        main_layout.addWidget(self.graphics_view)

        # Set the main layout for the QDialog
        self.setLayout(main_layout)
        QApplication.instance().installEventFilter(self)

        # Remove scroll bars
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        modules_by_categories = dict()
        self.module_categories = list()

        for module_name in self.available_modules:

            module_annotation = self.available_modules[module_name]

            category = module_annotation.module_category
            if category == "":
                category = "Standard"

            
            if category not in modules_by_categories:
                modules_by_categories[category] = list()

            modules_by_categories[category].append(module_name)
            self.module_categories.append(category)

        self.tabwidget = QTabWidget()
        self.tabwidget.setMaximumHeight(200)  #  the value as needed
        self.list_widgets_per_category = dict()
        for category_index, module_category in enumerate(modules_by_categories):
            module_list = [module_name for module_name in modules_by_categories[module_category]]

            # Create a list widget
            list_widget = QListWidget(self)
            list_widget.addItems(module_list)
            list_widget.setMaximumHeight(200)

            # Connect item selection changed signal to a function
            list_widget.itemSelectionChanged.connect(self.handle_list_selection)
            list_widget.setCurrentRow(0)    # For QListWidget, the currentRow needs to be set explicitly

            self.tabwidget.addTab(list_widget, module_category)
            self.list_widgets_per_category[category_index] = list_widget

        # Connect tab change signal to a function
        self.tabwidget.currentChanged.connect(self.handle_tab_change)
        self.handle_tab_change(0)   # For QTabWidget, the currentTab is already set to 0, thus need to call the function explicitly

        # Create Ok and Cancel buttons
        ok_button = QPushButton("Ok", self)
        cancel_button = QPushButton("Cancel", self)

        main_layout.addWidget(QLabel("Available Modules"))
        main_layout.addWidget(self.tabwidget)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        ok_button.clicked.connect(self.on_ok_button_clicked)
        cancel_button.clicked.connect(self.close_catalog)

        main_layout.addLayout(buttons_layout)

        # Set layout for the dialog
        self.setLayout(main_layout)
        self.update()
        self.graphics_view.setInteractive(False)

        self.resize(initial_width, initial_height)
        self.proxy_widget.widget().resize(self.graphics_view.width(), self.graphics_view.height())

        # self.on_module_selected(module_list[0])
        self.update()



    def scrollContentsBy(self, dx, dy):
        # Prevent horizontal scrolling
        print("Scroll")
        super().scrollContentsBy(0, dy)

    def resizeEvent(self, event):
        print("resize event")
        # Adjust the line's length to match the width of the QTextEdit
        print(event)

        new_size = event.size()

        # Extract width and height values
        width = new_size.width()
        height = new_size.height()

        min_size = 500
        print(width, height)
        print(width, height)
        if(width < min_size):
            width = min_size
            print("resize")
            self.resize(min_size, height)
            return
        
        if(height < min_size):
            height = min_size
            print("resize")
            self.resize(width, min_size)
            return

        y_pos = height * self.ratio_module_text


        print(self.graphics_view.height())
        self.line_item.setLine(0, y_pos, self.graphics_view.width(), y_pos)

        self.proxy_widget.setPos(0, y_pos + 10)  # Adjust the position as needed
        # self.proxy_widget.setRect(self.graphics_view.width(), self.graphics_view.height() * self.ratio_module_text)
        # self.proxy_widget.setGeometry(QRectF(0,height * self.ratio_module_text + 10, self.graphics_view.width(), height))

        self.module_text.setFixedHeight(self.calculate_text_height(self.module_text.toPlainText()))

        self.proxy_widget.widget().resize(self.graphics_view.width(), self.proxy_widget.widget().height())

        self.rect_item.setPos(self.graphics_view.width()//2 - self.rect_item.rect().width()//2, y_pos // 2 - self.module_height//2)

    def handle_list_selection(self):
        idx = self.tabwidget.currentIndex()
        if(idx == -1):
            return
        selected_item = self.list_widgets_per_category[idx].currentItem()
        if selected_item:
            # Call a function with the selected item's text
            self.on_module_selected(selected_item.text())

    def handle_tab_change(self, idx):
        if(idx == -1):
            return
        self.list_widgets_per_category[idx].setCurrentRow(0)
        selected_item = self.list_widgets_per_category[idx].currentItem()
        if selected_item:
            # Call a function with the selected item's text
            self.on_module_selected(selected_item.text())

    def on_module_selected(self, item_text):
        print(f"Selected item: {item_text}")
        self.show_information_for_module(item_text)

    def show_information_for_module(self, module_type: str):
        print("show info")
        module_annotation = self.available_modules[module_type]
        input_channels = self.claid.get_input_channels_of_module(module_annotation)
        output_channels = self.claid.get_output_channels_of_module(module_annotation)

        input_channel_types = self.claid.get_input_channel_types_of_module(module_annotation)
        output_channel_types = self.claid.get_output_channel_types_of_module(module_annotation)

        description = module_annotation.module_description
        # description = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   uis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet,"
        self.module_text.setText(description)
        self.module_text.setFixedHeight(self.calculate_text_height(description))

        self.generate_property_descriptions(module_annotation)
        self.generate_channel_descriptions(module_annotation)
        

        self.rect_item.set_channels(input_channels, output_channels, input_channel_types, output_channel_types)
        self.rect_item.set_type(module_type)
        self.rect_item.set_id("New Module")
        print("show info done")
        
    def generate_property_descriptions(self, module_annotation):
        
        self.properties_table.setRowCount(len(module_annotation.properties))
        self.properties_table.setColumnCount(2)

        self.properties_table.setHorizontalHeaderLabels(["Property", "Description"])

        ctr = 0

        for row in range(len(module_annotation.properties)):
            for col in range(2):
                if self.properties_table.item(row, col):
                    self.properties_table.item(row, col).setText("")
                else:
                    new_item = QTableWidgetItem("")
                    self.properties_table.setItem(row, col, new_item)

        for property, description in zip(module_annotation.properties, module_annotation.property_descriptions):
            self.properties_table.item(ctr, 0).setText(property)
            self.properties_table.item(ctr, 1).setText(description)
            self.properties_table.update()
            ctr += 1
            
    def generate_channel_descriptions(self, module_annotation):

        channels = module_annotation.channel_definition

        self.channels_table.setRowCount(len(channels))
        self.channels_table.setColumnCount(4) # Channel name, channel type, channel data type, channel description

        ctr = 0

        input_channels = list()
        input_channel_descriptions = list()
        output_channels = list()
        output_channel_descriptions = list()

        data_types_dict = dict()

        for channel, description in zip(module_annotation.channel_definition, module_annotation.channel_description):
            
            print(channel)
            data_types_dict[channel.channel] = channel.payload.message_type
            if channel.source_module != "":
                # Is output channel
                output_channels.append(channel.channel)
                output_channel_descriptions.append(description)

            elif channel.target_module != "":
                # Is input channel
                input_channels.append(channel.channel)
                input_channel_descriptions.append(description)

            else:
                raise ValueError("Invalud channel {}, cannot determine whether it is an input or output channel since neither source nor target are set.".format(channel.channel))

        for row in range(len(channels)):
            for col in range(4):
                if self.channels_table.item(row, col):
                    self.channels_table.item(row, col).setText("")
                else:
                    new_item = QTableWidgetItem("")
                    self.channels_table.setItem(row, col, new_item)
        

        for channel, description in zip(input_channels, input_channel_descriptions):
            self.channels_table.item(ctr, 0).setText(channel)
            self.channels_table.item(ctr, 1).setText("Input")
            self.channels_table.item(ctr, 2).setText(data_types_dict[channel])
            self.channels_table.item(ctr, 3).setText(description)
            print("ctr", ctr)
            ctr += 1

        for channel, description in zip(output_channels, output_channel_descriptions):
            self.channels_table.item(ctr, 0).setText(channel)
            self.channels_table.item(ctr, 1).setText("Output")
            self.channels_table.item(ctr, 2).setText(data_types_dict[channel])
            self.channels_table.item(ctr, 3).setText(description)
            print("ctr", ctr)
            ctr += 1

        self.channels_table.setHorizontalHeaderLabels(["Channel", "Channel type", "Data type", "Description"])

        self.channels_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.channels_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.channels_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.channels_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.channels_table.update()

    def on_ok_button_clicked(self):

        module_name, ok = QInputDialog().getText(self, "Module name",
                                     "Enter a unique name for the Module.", QLineEdit.Normal)
        if not ok or not module_name:
            return
        
        if self.parent_host.does_module_with_name_exist(module_name):
            QMessageBox.critical(None, "Error", "A Module with name \"{}\" already exists. Please choose an unique name for the Module.".format(module_name))

            return 

        idx = self.tabwidget.currentIndex()
        if(idx == -1):
            return
        
        list_widget = self.list_widgets_per_category[idx]
        module_type = list_widget.currentItem().text()
        module_annotation = self.available_modules[module_type]
        input_channels = self.claid.get_input_channels_of_module(module_annotation)
        output_channels = self.claid.get_output_channels_of_module(module_annotation)
        input_channel_types = self.claid.get_input_channel_types_of_module(module_annotation)
        output_channel_types = self.claid.get_output_channel_types_of_module(module_annotation)

        properties = module_annotation.properties
        property_descriptions = module_annotation.property_descriptions
        property_hints = module_annotation.property_hints

        empty_properties = [42]

        self.defined_properties = dict()

        self.__property_dialog_module_name = module_name
        self.property_dialog = PropertyInputDialog(properties, property_descriptions, property_hints)
        self.property_dialog.onOkButtonClicked.connect(self.onPropertyDialogOkClicked)

        if len(properties) > 0:
            self.property_dialog.open()
        else:
            self.onPropertyDialogOkClicked()

    def onPropertyDialogOkClicked(self):

        idx = self.tabwidget.currentIndex()
        if(idx == -1):
            return
        
        list_widget = self.list_widgets_per_category[idx]
        module_type = list_widget.currentItem().text()
        module_annotation = self.available_modules[module_type]
        input_channels = self.claid.get_input_channels_of_module(module_annotation)
        output_channels = self.claid.get_output_channels_of_module(module_annotation)
        input_channel_types = self.claid.get_input_channel_types_of_module(module_annotation)
        output_channel_types = self.claid.get_output_channel_types_of_module(module_annotation)

        properties = module_annotation.properties
        property_descriptions = module_annotation.property_descriptions
        property_hints = module_annotation.property_hints

        self.defined_properties = self.property_dialog.get_defined_properties()
        empty_properties = self.property_dialog.get_empty_properties()

        if len(empty_properties) != 0:

            empty_list_msg = ""
            for property in empty_properties:
                empty_list_msg += "\t\"" + str(property) +  "\"\n"
            QMessageBox.critical(None, "Undefined property", "You did not specify a value for the following properties:\n{}".format(empty_list_msg) + 
                                    "Please make sure that you define each property.")

            self.property_dialog = PropertyInputDialog(properties, property_descriptions, property_hints, self.defined_properties)
            self.property_dialog.onOkButtonClicked.connect(self.onPropertyDialogOkClicked)
            self.property_dialog.open()
            return

        # Add the module to the host
        host_width = self.parent_host.rect().width()
        host_height = self.parent_host.rect().height()
        host_title_bar_height = self.parent_host. get_title_bar_height()
        module_width = self.parent_host.get_module_width()
        module_height = self.parent_host.get_module_height()

        x = (host_width - module_width) / 2
        y = (host_height - module_height + host_title_bar_height) / 2
        module = self.parent_host.add_module(self.__property_dialog_module_name, module_type, x, y, input_channels, output_channels,\
                                              input_channel_types, output_channel_types, properties, property_descriptions, property_hints)
        module.set_properties(self.defined_properties)
        
        if self.module_injections_supported:
            module.set_is_injectable(module_annotation.is_injectable)
            module.set_injection_file_dependencies(module_annotation.file_dependencies)
        self.close_catalog()
    
    def close_catalog(self):
        self.close()
        self.on_catalog_closed.emit()


    def calculate_text_height(self, text):
        document = self.module_text.document()
        docHeight = document.size().height()
        print("HEIGHT ",
               docHeight)
        return int(docHeight)
    
 