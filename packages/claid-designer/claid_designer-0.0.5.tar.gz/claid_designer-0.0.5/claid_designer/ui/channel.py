from PyQt5.QtWidgets import QGraphicsObject, QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
from PyQt5.QtCore import QRectF, pyqtSignal, Qt, QEvent
from PyQt5.QtGui import QPen, QColor, QPainterPath


class Channel(QGraphicsObject):

    onChannelClicked = pyqtSignal(QGraphicsObject)

    def __init__(self, name: str, data_type, x: int, y: int, diameter: int, parent=None):
        #TODO: Cannot import ModuleGraphicsItem due to circular import issue
        # if parent == None or not isinstance(parent, ModuleGraphicsItem):
        #     raise ValueError("Parent of Channel has to be a ModuleGraphicsItem, and cannot be None")
        if parent != None:
            super(Channel, self).__init__(parent)
        else:
            super(Channel, self).__init__()
    
        self.module_parent = parent
        # Initialize major channel attributes
        self.name = name
        self.data_type = data_type

        # self.data_type = data_type
        print("Channel 2")

        # Set dimensions
        self.diameter = diameter

        # Set colors and thickness
        self.thickness = 2
        self.default_color = self.parentItem().get_color()
        self.default_pen = QPen(self.default_color, self.thickness)
        self.default_brush = QColor(self.default_color)
        self.hover_color = QColor("#548CCC")
        self.hover_pen = QPen(self.hover_color, self.thickness * 1.5)
        self.hover_brush = QColor(self.hover_color)
        self.click_color = QColor("#1A5CA8")
        self.click_pen = QPen(self.click_color, self.thickness * 1.5)
        self.click_brush = QColor(self.click_color)
        print("Channel 3")

        # Set position:
        self.setPos(x, y)

        # Check if it is input channel
        if x == 0:
            self.is_input = True
        else:
            self.is_input = False

        # Draw channel shape at initialization
        self.path = self.drawChannel()

        # Set flags
        self.setAcceptHoverEvents(True)
        self.hovered = False
        self.clicked = False
        print("Channel 4")


    def boundingRect(self):
        return self.path.boundingRect()

    def paint(self, painter, option, widget=None):
        # Set color and brush
        if self.isClicked():
            channel_pen = self.click_pen
            channel_brush = self.click_brush
        elif self.isHovered():
            channel_pen = self.hover_pen
            channel_brush = self.hover_brush
        else:
            channel_pen = self.default_pen
            channel_brush = self.default_brush
        painter.setPen(channel_pen)
        painter.setBrush(channel_brush)

        # Draw channel
        painter.drawPath(self.path)

    def hoverEnterEvent(self, event):
        self.hovered = True
        if self.parentItem().isHovered():
            self.parentItem().set_hovered(False)
        self.update()
        super(Channel, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.hovered = False
        self.update()
        super(Channel, self).hoverLeaveEvent(event)

    def mousePressEvent(self, event):
        # Clear selection of other GraphicsItems
        if not self.isSelected():
            self.scene().clearSelection()

        if event.button() == Qt.LeftButton:
            self.clicked = True
            self.update()
            self.onChannelClicked.emit(self)
        else:
            super(Channel, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked = False
            self.update()
        super(Channel, self).mouseReleaseEvent(event)

    def drawChannel(self) -> QPainterPath:
        path = QPainterPath()
        path.moveTo(0, 0)
        if self.is_input:
            path.lineTo((-self.diameter * 2/12), 0)
            path.arcTo((-self.diameter * 5/12), 0, (self.diameter * 6/12), self.diameter, 90, 180)
        else:
            path.lineTo((self.diameter * 2/12), 0)
            path.arcTo((-self.diameter * 1/12), 0, (self.diameter * 6/12), self.diameter, 90, -180)
        path.lineTo(0, self.diameter)
        path.closeSubpath()

        return path

    def get_name(self) -> str:
        return self.name

    def has_same_data_type_as_channel(self, other_channel):
        

        our_data_type_case = self.data_type.payload.message_type
        other_data_type_case = other_channel.get_data_type().payload.message_type

        print(our_data_type_case)
        print(other_data_type_case)

        # Temporary exception for the DataSaver
        if self.module_parent.get_type() == "DataSaverModule" or other_channel.module_parent.get_type() == "DataSaverModule":
            return True

        if our_data_type_case != other_data_type_case:
            return False
        
        if our_data_type_case == "blob_val":
            our_message_type = self.data_type.blob_val.message_type
            other_message_type = other_channel.get_data_type().blob_val.message_type

            if our_message_type != other_message_type:
                return False
            
        
        return True
    

    def get_data_type(self):
        return self.data_type
    
    def get_data_type_name(self):
        name = self.data_type.payload.message_type

        if name != "blob_val":
            return name
        
        return self.data_type.blob_val.message_type
    
    def get_name(self):
        return self.name

    def isClicked(self) -> bool:
        return self.clicked
    
    def isHovered(self) -> bool:
        return self.hovered
    
    def set_hovered(self, hovered: bool) -> None:
        self.hovered = hovered
        self.update()

    def set_default_color(self, color: QColor) -> None:
        self.default_color = color
        self.default_pen = QPen(self.default_color, self.thickness)
        self.default_brush = QColor(self.default_color)
        # self.update()
