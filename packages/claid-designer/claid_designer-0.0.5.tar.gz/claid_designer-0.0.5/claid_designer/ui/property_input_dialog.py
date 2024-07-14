import sys
from PyQt5.QtWidgets import QFileDialog, QComboBox, QLabel, QHeaderView, QFrame, QTableWidget, QTableWidgetItem, QWidget, QGraphicsWidget, QMessageBox, QErrorMessage, QInputDialog, QLineEdit, QApplication, QGraphicsScene, QGraphicsView, QGraphicsProxyWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QGraphicsRectItem, QGraphicsLineItem, QDialog, QSizePolicy, QListWidget, QPushButton
from PyQt5.QtCore import QPointF, Qt, QLineF, QSize, QRectF, pyqtSignal
from PyQt5.QtGui import QResizeEvent, QFontMetrics, QIntValidator

from ui.non_scrollable_graphics_view import NonScrollableGraphicsView

from claid.dispatch.proto.claidservice_pb2  import PropertyHint, PropertyType
import os
class PropertyInputDialog(QDialog):

    onOkButtonClicked = pyqtSignal()

    def __init__(self, properties, property_descriptions, property_hints, defined_properties = None):

        super().__init__()

        self.properties = properties
        self.property_descriptions = property_descriptions
        self.property_hints = property_hints

        if defined_properties == None:
            defined_properties = dict()

        # Set up the main layout
        main_layout = QVBoxLayout(self)

        self.__property_input_ui_elements = dict()
        self.__property_path_buttons = dict()

        self.was_cancelled = False

        main_layout.addWidget(QLabel("Please configure the properties of the Module.\nProperties:"))

        for property, description, property_hint in zip(properties, property_descriptions, property_hints):
            layout = QHBoxLayout()

            label = QLabel(property)
            label.setToolTip(description)
            layout.addWidget(label)

            property_ui_element = self.__add_property_ui_elements_according_to_property_type(property, description, property_hint, defined_properties)
            
            if isinstance(property_ui_element, list):
                for element in property_ui_element:
                    layout.addWidget(element)
            else:
                layout.addWidget(property_ui_element)
            main_layout.addLayout(layout)

            self.__property_input_ui_elements[property] = property_ui_element


        # Create Ok and Cancel buttons
        ok_button = QPushButton("Ok", self)
        cancel_button = QPushButton("Cancel", self)
        ok_button.clicked.connect(self.on_ok_button_clicked)
        cancel_button.clicked.connect(self.on_cancel_button_clicked)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)
        main_layout.addLayout(buttons_layout)

        # Set layout for the dialog
        self.setLayout(main_layout)

    def __add_property_ui_elements_according_to_property_type(self, property: str, property_description: str, property_hint: PropertyHint, defined_properties: dict):
        
        if property_hint.property_type == PropertyType.PROPERTY_TYPE_DEFAULT:
        
            line_edit = QLineEdit()
            line_edit.setToolTip(property_description)
            
            if property in defined_properties:
                line_edit.setText(defined_properties[property])

            return line_edit
        
        elif property_hint.property_type == PropertyType.PROPERTY_TYPE_ENUM:
            combobox = QComboBox()
            combobox.addItems(property_hint.property_type_enum_values)

            if property in defined_properties:
                combobox.setCurrentText(defined_properties[property])

            return combobox
        
        elif property_hint.property_type == PropertyType.PROPERTY_TYPE_INT:
        
            line_edit = QLineEdit()
            line_edit.setToolTip(property_description)
            validator = QIntValidator(property_hint.property_type_int_min, property_hint.property_type_int_max)
            line_edit.setValidator(validator)
            if property in defined_properties:
                line_edit.setText(defined_properties[property])

            return line_edit
        
        elif property_hint.property_type == PropertyType.PROPERTY_TYPE_PATH:
        
            horizontal_layout = QHBoxLayout()
            line_edit = QLineEdit()
            line_edit.setToolTip(property_description)
            
            if property in defined_properties:
                line_edit.setText(defined_properties[property])


            button = QPushButton("...")
            button.clicked.connect(lambda _, button=button: self.on_path_button_clicked(button))
            self.__property_path_buttons[button] = property
            return [line_edit, button]
        

    def get_defined_properties(self):

        properties = dict()
        for property in self.properties:

         
            value = self.__get_property_value_from_ui_element(property)

            if value != "":
                properties[property] = value

        return properties
    
    def get_empty_properties(self):

        empty_properties = list()
        for property in self.properties:
            
            value = self.__get_property_value_from_ui_element(property)

            if value == "":
                empty_properties.append(property)

        return empty_properties

    def __get_property_value_from_ui_element(self, property):

        if property not in self.__property_input_ui_elements:
            return ""
        
        ui_element = self.__property_input_ui_elements[property]

        property_hint = None

        for i in range(len(self.properties)):
            if self.properties[i] == property:
                property_hint = self.property_hints[i]

        if property_hint == None:
            raise ValueError("Failed to get property_hint of property \"{}\"".format(property))
        property_type = property_hint.property_type

        if property_type == PropertyType.PROPERTY_TYPE_DEFAULT or property_type == PropertyType.PROPERTY_TYPE_INT:
            return ui_element.text()

        elif property_type == PropertyType.PROPERTY_TYPE_ENUM:
            return ui_element.currentText()
        
        elif property_type == PropertyType.PROPERTY_TYPE_PATH:
            return ui_element[0].text()

    def on_ok_button_clicked(self):

        if not self.verify_properties():
            return
        self.was_cancelled = False
        self.close()
        self.onOkButtonClicked.emit()

    def verify_properties(self):
        
        for property, property_hint in zip(self.properties, self.property_hints):
            if property_hint.property_type == PropertyType.PROPERTY_TYPE_INT:
                line_edit = self.__property_input_ui_elements[property]

                input_text = line_edit.text()
                try:
                    number = int(input_text)

                    if number < property_hint.property_type_int_min or number > property_hint.property_type_int_max:
                        QMessageBox.critical(None, "Out of range", "Value {} of property \"{}\" is out of range [{},{}]. Please choose a value within the range.".format(\
                            number, property, property_hint.property_type_int_min, property_hint.property_type_int_max))
                        return False
                except Exception as e:
                    QMessageBox.critical(None, "Out of range", "Value {} of property \"{}\" is not a number. Please choose a value in the range [{},{}]".format(\
                            input_text, property, property_hint.property_type_int_min, property_hint.property_type_int_max))
                    return False

        return True


    def on_cancel_button_clicked(self):
        self.was_cancelled = True
        self.close()

    def ok(self):
        return not self.was_cancelled
    
    def cancelled(self):
        return self.was_cancelled
    
    def on_path_button_clicked(self, button):
        directory_path = QFileDialog.getExistingDirectory(self, 'Select Directory', os.getcwd())
        
        if not directory_path:
            return
        
        clicked_property_name = self.__property_path_buttons[button]

        ui_element = self.__property_input_ui_elements[clicked_property_name]
        line_edit = ui_element[0]
        line_edit.setText(directory_path) 
