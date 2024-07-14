from PyQt5.QtWidgets import QGraphicsPathItem, QGraphicsSceneHoverEvent, QMenu, QAction
from PyQt5.QtGui import QPainterPath, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, pyqtSignal

from ui.module_graphics_item import ModuleGraphicsItem


class PathGraphicsItem(QGraphicsPathItem):

    def __init__(self, path: QPainterPath, parent=None):
        self.hovered = False

        if parent != None:
            super(PathGraphicsItem, self).__init__(parent)
        else:
            super(PathGraphicsItem, self).__init__()

        #TODO: Would it make sense to add createPath and calculatePath methods to this class?

        # Initialize major path attributes
        self.setPath(path)

        # Set colors and thickness
        self.thickness = 2.5
        self.default_color = QColor("#2C6EBE")
        self.default_pen = QPen(self.default_color, self.thickness)
        self.default_brush = QBrush(self.default_color)
        self.hover_color = QColor("#BBDEFB")
        self.hover_pen = QPen(self.hover_color, self.thickness * 1.5)
        self.hover_brush = QBrush(self.hover_color)
        self.select_color = QColor("#37474F")
        self.select_pen = QPen(self.select_color, self.thickness * 1.5)
        self.select_brush = QBrush(self.select_color)

        # Input and output modules
        self.input_module = None
        self.output_module = None

        # Move path in front of other QGraphicsItems
        # Explanation: Hosts and paths are both childs of the scene
        # Thus, you can use z-values to control the order of these items
        self.setZValue(1)

        # Set flags
        self.setFlag(QGraphicsPathItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsPathItem.ItemIsFocusable, True)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        self.hovered = True
        self.update()
        super(PathGraphicsItem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.hovered = False
        self.update()
        super(PathGraphicsItem, self).hoverLeaveEvent(event)
    
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Delete) or (event.key() == Qt.Key_Backspace):
            self.deleteItem()
    
    def contextMenuEvent(self, event):
        self.context_menu = QMenu()
        delete_action = QAction("Delete", self.context_menu)
        delete_action.triggered.connect(self.deleteItem)
        self.context_menu.addAction(delete_action)
        self.context_menu.popup(event.screenPos())

    def deleteItem(self):
        # Remove paths from all lists and dicts
        self.output_module.delete_path(self)
        self.input_module.delete_path(self)

        # Remove path from scene
        scene = self.scene()
        scene.removeItem(self)

        # Delete path
        del self
        
    def paint(self, painter, option, widget):
        # Set color and brush
        if self.isSelected():
            path_pen = self.select_pen
            path_brush = self.select_brush
        elif self.isHovered():
            path_pen = self.hover_pen
            path_brush = self.hover_brush
        else:
            path_pen = self.default_pen
            path_brush = self.default_brush
        painter.setPen(path_pen)
        painter.setBrush(path_brush)

        # Draw path
        painter.drawPath(self.path())

    def get_input_module(self) -> ModuleGraphicsItem:
        return self.input_module
    
    def get_output_module(self) -> ModuleGraphicsItem:
        return self.output_module
    
    def set_input_module(self, module: ModuleGraphicsItem) -> None:
        self.input_module = module

    def set_output_module(self, module: ModuleGraphicsItem) -> None:
        self.output_module = module

    def isHovered(self) -> bool:
        return self.hovered

    def set_hovered(self, hovered: bool) -> None:
        self.hovered = hovered