import sys
from PyQt5.QtWidgets import QTabWidget, QLabel, QHeaderView, QFrame, QTableWidget, QTableWidgetItem, QWidget, QGraphicsWidget, QMessageBox, QErrorMessage, QInputDialog, QLineEdit, QApplication, QGraphicsScene, QGraphicsView, QGraphicsProxyWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QGraphicsRectItem, QGraphicsLineItem, QDialog, QSizePolicy, QListWidget, QPushButton
from PyQt5.QtCore import QPointF, Qt, QLineF, QSize, QRectF
from PyQt5.QtGui import QResizeEvent, QFontMetrics


from claid import CLAID
from claid.dispatch.proto.claidservice_pb2  import CLAIDConfig, ModuleAnnotation, DataPackage


class LogMessageView(QWidget):

    def __init__(self):
        super().__init__()

