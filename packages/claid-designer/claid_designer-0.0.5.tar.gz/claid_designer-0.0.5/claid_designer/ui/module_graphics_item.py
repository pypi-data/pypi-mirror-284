from PyQt5.QtWidgets import QMessageBox, QGraphicsItem, QGraphicsObject, QGraphicsTextItem, QMenu, QAction, QApplication
from PyQt5.QtGui import QFontMetrics, QColor, QPen, QBrush, QPainterPath, QFont
from PyQt5.QtCore import Qt, QRectF, pyqtSignal, QPointF
from ui.property_input_dialog import PropertyInputDialog

from ui.channel import Channel
import sip


class ModuleGraphicsItem(QGraphicsObject):
    
    onModuleItemMoved = pyqtSignal(QGraphicsObject, QPointF)
    pathDeleted = pyqtSignal(QGraphicsItem)
    onInjectableModuleMoveOutsideHost = pyqtSignal(QGraphicsObject) 

    def __init__(self, id: str, type: str, x: int, y: int, width: int, height: int, input_channels: list, output_channels: list, \
                 input_channel_types: dict, output_channel_types: dict, property_names: list, property_descriptions: list, property_hints: list, parent=None, movable=True):
        #! Could I also move this downwoards?
        self.movable = movable
        self.hovered = False

        if parent != None:
            super(ModuleGraphicsItem, self).__init__(parent)
        else:
            super(ModuleGraphicsItem, self).__init__()
        
        # Initialize major module attributes
        self.id = id
        self.type = type
        self.input_channel_map = dict()
        self.output_channel_map = dict()
        self.input_channel_text_map = dict()
        self.output_channel_text_map = dict()
        self.properties = dict()

        self.property_names = property_names
        self.property_descriptions = property_descriptions
        self.property_hints = property_hints

        self.injectable = False
        self.injected = False

        # Set dimensions
        self.width = width
        self.height = height

        # Set colors and thickness:
        self.thickness = 2
        self.corner_radius = 10
        self.default_color = QColor("#2C6EBE")
        self.default_pen = QPen(self.default_color, self.thickness)
        self.default_brush = QBrush(self.default_color)
        self.hover_color = QColor("#BBDEFB")
        self.hover_pen = QPen(self.hover_color, self.thickness * 1.5)
        self.hover_brush = QBrush(self.hover_color)
        self.select_color = QColor("#37474F")
        self.select_pen = QPen(self.select_color, self.thickness * 1.5)
        self.select_brush = QBrush(self.select_color)

        # #TODO: Just for demonstration purpose. Delete later
        # if self.id == "Module3":
        #     self.set_default_color(QColor("#D32F2F"))

        # Set position && connect signals
        if parent != None:
            parent_rect = self.parentItem().rect()
            self.setPos(parent_rect.left() + x, parent_rect.top() + y)
            
            parent.onHostItemResized.connect(self.onHostItemResized)
            parent.onHostItemMoved.connect(self.onHostItemMoved)
       
        # Set input and output channels
        self.set_channels(input_channels, output_channels, input_channel_types, output_channel_types)

        # List of connected paths
        self.paths = list()

        # Set flags
        self.mouseMove = False
        if movable:
            self.setFlag(QGraphicsItem.ItemIsMovable, True)
            self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
            self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)

        self.item_was_moved = False

        self.injection_file_dependencies = []

    def boundingRect(self):
        return self.rectf
    
    def rect(self):
        return self.rectf
    
    def setRect(self, x, y, new_width, new_height):
        self.rectf = QRectF(x, y, new_width, new_height)
        self.update()

    def hoverEnterEvent(self, event):
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.corner_radius, self.corner_radius)
        if path.contains(event.pos()):
            self.hovered = True
            self.update()
        super(ModuleGraphicsItem, self).hoverEnterEvent(event)

    def hoverMoveEvent(self, event):
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.corner_radius, self.corner_radius)
        if path.contains(event.pos()):
            self.hovered = True
            self.update()
        super(ModuleGraphicsItem, self).hoverMoveEvent(event)

    def hoverLeaveEvent(self, event):
        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.corner_radius, self.corner_radius)
        if not path.contains(event.pos()):
            self.hovered = False
            self.update()
        super(ModuleGraphicsItem, self).hoverLeaveEvent(event)
    
    def mousePressEvent(self, event):
        # Give focus to the item when clicked
        self.setFocus()
        self.item_was_moved = False
        # Clear selection of other GraphicsItems
        if not self.isSelected():
            self.scene().clearSelection()

        if event.button() == Qt.LeftButton:
            self.mousePressPos = event.pos()
            self.origPos = self.pos()
            self.mouseMove = False
        super(ModuleGraphicsItem, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.mouseMove = True
        super(ModuleGraphicsItem, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.check_if_module_was_moved_outside_host()

            if not self.mouseMove:
                # Handle click event here if needed
                pass
        super(ModuleGraphicsItem, self).mouseReleaseEvent(event)

    def check_if_module_was_moved_outside_host(self):
        print("mouse release event, ", self.item_was_moved)

        if(not self.is_inside_host(self.parentItem())):
            self.onInjectableModuleMoveOutsideHost.emit(self)
  
    def is_inside_host(self, host):
        bounding_rect1 = self.mapToScene(self.rect()).boundingRect()
        bounding_rect2 = host.mapToScene(host.rect()).boundingRect()
        return bounding_rect2.contains(bounding_rect1)


    def itemChange(self, change, value):
        if not self.movable:
            return super(ModuleGraphicsItem, self).itemChange(change, value)

        if change == QGraphicsItem.ItemPositionChange:
            new_pos = value
            changed_pos = self.restrictMovement(new_pos)
            absolute_change = changed_pos - self.pos()
            self.onModuleItemMoved.emit(self, absolute_change)
            self.item_was_moved = True
            return super(ModuleGraphicsItem, self).itemChange(change, changed_pos)
        else:
            return super(ModuleGraphicsItem, self).itemChange(change, value)
    
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Delete) or (event.key() == Qt.Key_Backspace):
            self.deleteItem()
    
    def contextMenuEvent(self, event):
        self.context_menu = QMenu()
        delete_action = QAction("Delete", self.context_menu)
        delete_action.triggered.connect(self.deleteItem)
        properties_action = QAction("Show Properties", self.context_menu)
        properties_action.triggered.connect(self.showProperties)
        self.context_menu.addAction(delete_action)
        self.context_menu.addAction(properties_action)
        self.context_menu.popup(event.screenPos())

    def deleteItem(self):
        # Ask for confirmation
        reply = QMessageBox.question(None, "Delete module", "Do you really want to delete this module and its connections to other modules?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        # Remove modules from all lists
        self.parentItem().delete_module(self.id)

        # Delete paths
        while self.paths:
            path = self.paths[0]
            path.deleteItem()

        # Remove module from scene
        scene = self.scene()
        scene.removeItem(self)

        # Delete module
        del self
    
    def showProperties(self):
        empty_properties = [42]

        print("Show properties ", self.property_names, len(empty_properties), len(self.property_names))
        defined_properties = self.properties

        if len(self.property_names) == 0:
            QMessageBox.information(None, "No properties", "This Module has no properties.")
            return

  
        self.property_dialog = PropertyInputDialog(self.property_names, self.property_descriptions, self.property_hints, defined_properties=self.properties)
        self.property_dialog.onOkButtonClicked.connect(self.onPropertyDialogOkClicked)
        self.property_dialog.open()

    def onPropertyDialogOkClicked(self):
       
        defined_properties = self.property_dialog.get_defined_properties()
        empty_properties = self.property_dialog.get_empty_properties()

        if len(empty_properties) != 0:

            empty_list_msg = ""
            for property in empty_properties:
                empty_list_msg += "\t\"" + str(property) +  "\"\n"
            QMessageBox.critical(None, "Undefined property", "You did not specify a value for the following properties:\n{}".format(empty_list_msg) + 
                                    "Please make sure that you define each property.")

            self.property_dialog = PropertyInputDialog(self.property_names, self.property_descriptions, self.property_hints, defined_properties=self.properties)
            self.property_dialog.onOkButtonClicked.connect(self.onPropertyDialogOkClicked)
            self.property_dialog.open()
            return

        self.properties = defined_properties
        
    def restrictMovement(self, new_pos):
        if not self.movable:
            return new_pos
        
        if self.injectable:
            return new_pos

        parent_rect = self.parentItem().rect()
        item_rect = self.boundingRect()
        parent_title_bar_height = self.parentItem().get_title_bar_height()

        # Restrict movement horizontally
        if new_pos.x() < parent_rect.left():
            new_pos.setX(parent_rect.left())
        elif new_pos.x() + item_rect.width() > parent_rect.right():
            new_pos.setX(parent_rect.right() - item_rect.width())

        # Restrict movement vertically
        if new_pos.y() < parent_rect.top() + parent_title_bar_height:
            new_pos.setY(parent_rect.top() + parent_title_bar_height)
        elif new_pos.y() + item_rect.height() > parent_rect.bottom():
            new_pos.setY(parent_rect.bottom() - item_rect.height())

        #TODO: Prevent that modules can collide
        # self_scene_rect = self.mapRectToScene(item_rect)
        # self_scene_rect.moveTo(new_pos)
        # for module in self.parentItem().childItems():
        #     if isinstance(module, ModuleGraphicsItem):
        #         if module != self:
        #             module_scene_rect = module.mapRectToScene(module.boundingRect().marginsAdded(QMarginsF(1, 1, 1, 1)))
        #             if self_scene_rect.intersects(module_scene_rect):
        #                 new_pos = self.pos()

        return new_pos

    def onHostItemResized(self, new_width, new_height):
        self.setPos(self.restrictMovement(self.pos()))
        self.update()

    def onHostItemMoved(self, host, change):
        absolute_change = change
        self.onModuleItemMoved.emit(self, absolute_change)

    def paint(self, painter, option, widget):
        self.repaint(painter)

    def repaint(self, painter):
        if self.isSelected():
            module_pen = self.select_pen
            module_brush = self.select_brush
            for child in self.childItems():
                if isinstance(child, Channel):
                    child.set_default_color(self.select_color)
                    child.update()
        elif self.isHovered():
            module_pen = self.hover_pen
            module_brush = self.hover_brush
            for child in self.childItems():
                if isinstance(child, Channel):
                    child.set_default_color(self.hover_color)
                    child.update()
        else:
            module_pen = self.default_pen
            module_brush = self.default_brush
            for child in self.childItems():
                if isinstance(child, Channel):
                    child.set_default_color(self.default_color)
                    # Attention: child.update() is not called explicitly here 
                    # bcs it seems to be called anyways and would cause a crash
                    # when module catalog is opened after adding a module 
        
        # Draw rectangle
        rect = self.rect()
        painter.setPen(module_pen)
        painter.setBrush(Qt.white)
        painter.drawRoundedRect(rect, self.corner_radius, self.corner_radius)

        # Draw smaller rectangle at the top for the module_type text
        x = rect.x()
        y = rect.y()
        width = rect.width()
        height = rect.height()

        font_metrics = painter.fontMetrics()
        text_content_type = font_metrics.elidedText(self.type, Qt.ElideRight, width)#+ " | Java")
        text_dimensions_type = painter.boundingRect(QRectF(), Qt.AlignLeft, text_content_type)
        text_rect_type_width = text_dimensions_type.width()
        text_rect_type_height = 1.35 * text_dimensions_type.height()
        text_rect_type = QRectF(x, y, width, text_rect_type_height)

        path = QPainterPath()
        path.moveTo(text_rect_type.left(), text_rect_type.top() + self.corner_radius)
        path.arcTo(text_rect_type.left(), text_rect_type.top(), 2 * self.corner_radius, 2 * self.corner_radius, 180, -90)
        path.lineTo(text_rect_type.right() - self.corner_radius, text_rect_type.top())
        path.arcTo(text_rect_type.right() - 2 * self.corner_radius, text_rect_type.top(), 2 * self.corner_radius, 2 * self.corner_radius, 90, -90)
        path.lineTo(text_rect_type.right(), text_rect_type.bottom())
        path.lineTo(text_rect_type.left(), text_rect_type.bottom())
        path.closeSubpath()
        painter.setBrush(module_brush)
        painter.drawPath(path)

        # Set color for module_type text
        painter.setPen(Qt.white)

        # Draw module_type text
        x_position = x + (width / 2) - (text_rect_type_width / 2)
        y_position = y + text_dimensions_type.height()
        painter.drawText(int(x_position), int(y_position), text_content_type) #+ " | Java")        
        
        # Set color for module_id text
        painter.setPen(Qt.black)

        # Draw module_id text
        text_content_id = font_metrics.elidedText(self.id, Qt.ElideRight, width)
        text_dimensions_id = painter.boundingRect(QRectF(), Qt.AlignLeft, text_content_id)
        text_rect_id_width = text_dimensions_id.width()
        text_rect_id_height = text_dimensions_id.height()

        x_position = x + (width / 2) - (text_rect_id_width / 2)
        y_position = y + ((height + text_rect_type_height) / 2) + (text_rect_id_height / 2) - font_metrics.descent()
        painter.drawText(int(x_position), int(y_position), text_content_id)

    def add_path(self, path):
        self.paths.append(path)

    def delete_path(self, path):
        self.paths.remove(path)
        self.pathDeleted.emit(path)

    def get_color(self) -> QColor:
        color = self.default_color
        return color

    def set_default_color(self, color: QColor) -> None:
        self.default_color = color
        self.default_pen = QPen(self.default_color, self.thickness)
        self.default_brush = QBrush(self.default_color)
        # Use this color for errors or warnings: #D32F2F
        self.update()

    def set_id(self, name: str):
        self.id = name
        self.update()

    def get_id(self) -> str:
        return self.id
    
    def set_type(self, type: str):
        self.type = type
        #TODO: When this is also drawn in the module (via (re)paint function), I need to call update() 
        # self.update()

    def get_type(self) -> str:
        return self.type

    def set_channels(self, input_channels, output_channels, input_channel_types, output_channel_types) -> None:

        # Create a rectangle that represents the module
        width = self.width
        height = self.height
        self.rectf = QRectF(0, 0, width, height)
        print("mod dim", self.width, self.height)
        for channel in self.input_channel_map.values():
            print("delete")
            sip.delete(channel)
        self.input_channel_map.clear()

        for channel in self.output_channel_map.values():
            sip.delete(channel)
        self.output_channel_map.clear()

        for text in self.input_channel_text_map.values():
            sip.delete(text)
        self.input_channel_text_map.clear()

        for text in self.output_channel_text_map.values():
            sip.delete(text)
        self.output_channel_text_map.clear()


        # Calculate position of input and output channels
        self.circle_diameter = min(width, height) * 0.125
        circle_diameter = self.circle_diameter
        input_x_pos = 0 
        output_x_pos = width
        self.num_input_channels = len(input_channels)
        self.num_output_channels = len(output_channels)
        input_y_distance = height / (self.num_input_channels + 1)
        input_y_pos = input_y_distance - (circle_diameter / 2)
        output_y_distance = height / (self.num_output_channels + 1)
        output_y_pos = output_y_distance - (circle_diameter / 2)
        text_x_offset = 10
        text_y_offset = 1
        font_size = 10
        adjustment = 4  # Somehow to the text always starts a bit too far to the right (and to the top)

        print("dbg 1")
        for input_channel in input_channels:

            if not input_channel in input_channel_types:
                raise ValueError("Unable to find data type of input channel {}".format(input_channel))
            
            data_type = input_channel_types[input_channel]
            print("dbg 2")

            self.input_channel_map[input_channel] = Channel(input_channel, data_type, input_x_pos, input_y_pos, circle_diameter, self)
            self.input_channel_text_map[input_channel] = QGraphicsTextItem(input_channel, self)
            self.input_channel_text_map[input_channel].setDefaultTextColor(Qt.black)
            text_font = self.input_channel_text_map[input_channel].font()
            text_font.setPointSize(font_size)
            self.input_channel_text_map[input_channel].setFont(text_font)
            text_dim = QFontMetrics(text_font)
            text_width = text_dim.width(self.input_channel_text_map[input_channel].toPlainText())
            text_height = text_dim.height()
            text_x_pos = -text_width - text_x_offset - adjustment
            text_y_pos = input_y_pos - text_height - text_y_offset
            self.input_channel_text_map[input_channel].setPos(text_x_pos, text_y_pos)
            input_y_pos += input_y_distance
        for output_channel in output_channels:
            if not output_channel in output_channel_types:
                raise ValueError("Unable to find data type of input channel {}".format(output_channel))
            
            data_type = output_channel_types[output_channel]

            self.output_channel_map[output_channel] = Channel(output_channel, data_type, output_x_pos, output_y_pos, circle_diameter, self)
            self.output_channel_text_map[output_channel] = QGraphicsTextItem(output_channel, self)
            self.output_channel_text_map[output_channel].setDefaultTextColor(Qt.black)
            text_font = self.output_channel_text_map[output_channel].font()
            text_font.setPointSize(font_size)
            self.output_channel_text_map[output_channel].setFont(text_font)
            text_dim = QFontMetrics(self.output_channel_text_map[output_channel].font())
            text_width = text_dim.width(self.output_channel_text_map[output_channel].toPlainText())
            text_height = text_dim.height()
            text_x_pos = width + text_x_offset - adjustment
            text_y_pos = output_y_pos - text_height - text_y_offset
            self.output_channel_text_map[output_channel].setPos(text_x_pos, text_y_pos)
            output_y_pos += output_y_distance
        
        self.update()

    def get_input_channels(self) -> dict:
        return self.input_channel_map
    
    def get_output_channels(self) -> dict:
        return self.output_channel_map

    def get_properties(self) -> dict:
        return self.properties
    
    def set_properties(self, properties) -> None:
        self.properties = properties
    
    # def get_property_names(self) -> list:
    #     return self.property_names
    
    # def get_property_descriptions(self) -> list:
    #     return self.property_descriptions
    
    # def get_property_hints(self) -> list:
    #     return self.property_hints
    
    def set_hovered(self, hovered: bool) -> None:
        self.hovered = hovered
        self.update()
    
    def isHovered(self) -> bool:
        return self.hovered
    
    def set_is_injectable(self, injectable):
        self.injectable = injectable

    def is_injectable(self):
        return self.injectable

    def set_was_injected(self, injected):
        self.injected = injected

    def was_injected(self):
        return self.injected

    def set_injection_file_dependencies(self, dependencies: list):
        self.injection_file_dependencies = dependencies

    def get_injection_file_dependencies(self):
        return self.injection_file_dependencies 
