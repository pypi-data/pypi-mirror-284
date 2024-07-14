from PyQt5.QtWidgets import QSpacerItem, QTabWidget, QLabel, QHeaderView, QFrame, QTableWidget, QTableWidgetItem, QWidget, QGraphicsWidget, QMessageBox, QErrorMessage, QInputDialog, QLineEdit, QApplication, QGraphicsScene, QGraphicsView, QGraphicsProxyWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QGraphicsRectItem, QGraphicsLineItem, QDialog, QSizePolicy, QListWidget, QPushButton, QGraphicsOpacityEffect
from PyQt5.QtCore import QPointF, Qt, QLineF, QSize, QRectF, QPropertyAnimation, QPoint, QPropertyAnimation, QSequentialAnimationGroup, QParallelAnimationGroup, pyqtSignal
from PyQt5.QtGui import QResizeEvent, QFontMetrics, QMouseEvent, QFont, QPixmap

import os
import json
import ipaddress
import sys

from ui.animated_button import AnimatedButton


class LandingPage(QWidget):
        
    on_start_clicked = pyqtSignal(str)


    def __init__(self):
        super().__init__()

        self.init_ui()
        self.dragging = False
        self.ip = ""

    def init_ui(self):
        # Set up the main layout
        layout = QVBoxLayout(self)

        # Set the size to 7/10 of the screen width and height
        screen_rect = QApplication.desktop().screenGeometry()
        self.width = screen_rect.width() // 10 * 7
        self.height = screen_rect.height() // 10 * 7

        initial_x = (screen_rect.width() - self.width) // 2
        initial_y = (screen_rect.height() - self.height) // 2

        self.setGeometry(initial_x, initial_y, self.width, self.height)

        # Set the blue background
        self.setStyleSheet("background-color: #2094f3;")

        # Remove menu bar and toolbar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint)

        # Workshop title
        layout.addStretch(6)
        title = QLabel("From Code to Wrist: Innovating Healthcare with the CLAID Middleware for ML Deployment", self)
        title.setFont(QFont("Arial", 20, QFont.Bold, False))
        title.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        title.setStyleSheet("color: #FFFFFF")
        layout.addWidget(title)
        layout.addStretch(14)

        # CLAID title
        label = QLabel("CLAID: Closing the Loop on AI & Data Collection", self)
        label.setFont(QFont("Arial", 36, QFont.Bold, False))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #FFFFFF")
        layout.addWidget(label)
        layout.addStretch(3)

        # Add a QLineEdit for the user to enter the IP address
        self.line_edit = QLineEdit(self)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setMinimumWidth(200)
        self.line_edit.setMinimumHeight(25)
        self.line_edit.returnPressed.connect(self.start_button_clicked)
        self.line_edit.setStyleSheet("QLineEdit { background-color: white; color: black; border-radius: 5px; } QLineEdit::placeholder { color: gray; }")

        self.opacity_effect = QGraphicsOpacityEffect(self.line_edit)
        self.opacity_effect.setOpacity(0.0)  # Set initial opacity to 0.0
        self.line_edit.setGraphicsEffect(self.opacity_effect)
        layout.addWidget(self.line_edit, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        
         # Centered rounded Start button
        self.start_button = AnimatedButton("Begin")
        self.start_button.setStyleSheet("QPushButton { font-family: Arial, sans-serif; font-size: 18px; font-weight: bold; background-color: #F03434; color: white; border: none; border-radius: 10px; }"
                                    "QPushButton:hover { background-color: #FF4E4E; }"
                                    "QPushButton:pressed { background-color: #C0392B; }")
        self.start_button.setMinimumWidth(200)
        self.start_button.setMinimumHeight(50)
        self.start_button.clicked.connect(self.start_button_clicked)
        layout.addWidget(self.start_button, alignment=Qt.AlignCenter)

        # Create a horizontal layout to contain the text, icon, and link horizontally
        info_layout = QHBoxLayout()

        # Informational text label
        info_layout.addStretch()
        info_text = QLabel("For more information, visit our website:")
        info_text.setFont(QFont("Arial", 16))
        info_text.setStyleSheet("color: #FFFFFF")
        info_layout.addWidget(info_text)

        # Icon label
        icon_label = QLabel(self)

        current_file_path = os.path.abspath(__file__)
        # Get the directory containing the currently executed Python file
        current_directory = os.path.dirname(current_file_path)
        globe_icon = QPixmap(os.path.join(current_directory, "icons/globe.png"))
        icon_label.setPixmap(globe_icon.scaledToHeight(20, Qt.SmoothTransformation))
        info_layout.addWidget(icon_label)

        # Link label
        link_label = QLabel(self)
        link_label.setText('<a href="https://claid.ethz.ch" '
                           'style="color: #FFFFFF; text-decoration: underline;">'
                           'claid.ch</a>')
        link_label.setOpenExternalLinks(True)
        link_label.setFont(QFont("Arial", 16))
        link_label.setAlignment(Qt.AlignCenter)
        info_layout.addWidget(link_label)
        info_layout.addStretch()

        # Add the horizontal layout to the main vertical layout
        layout.addLayout(info_layout)
        layout.addStretch(24)

        # Add pictures and speakers side by side at the bottom 
        picture_layout = QHBoxLayout()
        current_path = os.path.abspath(os.path.dirname(__file__))

        # ETH logo
        picture1 = QLabel(self)
        pixmap1 = QPixmap(os.path.join(current_path, "images", "eth_logo.png"))
        picture1.setPixmap(pixmap1.scaledToHeight(100, Qt.SmoothTransformation))
        picture1.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        picture_layout.addWidget(picture1)

        # Speakers label
        speakers = QLabel("""<b>Speakers:</b><br>
                          Patrick Langer (planger@ethz.ch)<br>
                          Filipe Barata (fbarata@ethz.ch)<br>
                          Jinjoo Shim (jshim@ethz.ch)<br>
                          Fan Wu (fanwu@ethz.ch)""", self)
        speakers.setFont(QFont("Arial", 16))
        speakers.setStyleSheet("QLabel { color: #FFFFFF; border: 2px solid white; border-radius: 10px; padding: 10px; }")
        speakers.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        picture_layout.addWidget(speakers)

        # AMLD workshop image
        picture2 = QLabel(self)
        pixmap2 = QPixmap(os.path.join(current_path, "images", "embc_logo.png"))
        picture2.setPixmap(pixmap2.scaledToHeight(170, Qt.SmoothTransformation))
        picture2.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        picture_layout.addWidget(picture2)
        layout.addLayout(picture_layout)

        # Add the close button ("X") to the top right corner
        close_button = QPushButton("X", self)
        close_button.setGeometry(self.width - 30, 10, 20, 20)
        close_button.clicked.connect(self.close_exit)
        close_button.setStyleSheet("QPushButton { background-color: none; color: white; border: none; }"
            "QPushButton:hover { background-color: #D3D3D3; }"
            "QPushButton:pressed { background-color: #A9A9A9; }"
        )

        self.begin_clicked = False


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def close_window(self):
        self.close()

    def close_exit(self):
        os._exit(0)

    def start_button_clicked(self):

        if self.begin_clicked:

            ip_address_str = self.line_edit.text()
            ip_address_str = ip_address_str.strip()     # Strip leading and trailing whitespace
            valid = False
            exception = None
            try:
                ip, port = ip_address_str.split(":")
                port = int(port)
                addr = ipaddress.ip_address(ip)
                valid = True
            except Exception as e:
                valid = False
                exception = e

          
            if not valid:
                QMessageBox.critical(None, "Invalid IP4 Address", "The value \"{}\" is not a valid IPv4 address:\n{}".format(ip_address_str, str(exception)))
                return

            self.ip = ip_address_str
            self.save_ip_address(ip_address_str)    # Save the IP address for future sessions
            # self.on_start_clicked.emit(ip_address_str)
            self.close_window()
            return
        
        # If the user has not clicked the "Begin" button yet:
        self.begin_clicked = True

        # Animate the appearance of the QLineEdit
        self.line_edit.setHidden(False)
        self.line_edit.clear()
        self.animate_line_edit()

    def animate_line_edit(self):

        # If IP address was already entered in a previous session, display it
        try:
            with open('last_ip.json', 'r') as f:
                last_ip = json.load(f)
                self.line_edit.setText(last_ip)
        except FileNotFoundError:
            pass
        
        # Prepare changes to the QLineEdit and button
        self.setFocus()
        self.start_button.setText("Start CLAID")
        start_pos = QPoint(self.line_edit.geometry().left(), self.start_button.geometry().top())
        end_pos = self.line_edit.pos()
        self.line_edit.setPlaceholderText("Enter Smartwatch IP:Port")

        # Animate the position of the QLineEdit
        self.animation = QPropertyAnimation(self.line_edit, b'pos')
        self.animation.setStartValue(start_pos)
        self.animation.setEndValue(end_pos)
        self.animation.setDuration(100)  # Adjust the duration as needed

        # Animate the opacity of the QGraphicsOpacityEffect
        self.opacity_animation = QPropertyAnimation(self.line_edit.graphicsEffect(), b'opacity')
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(100)
        self.opacity_animation.setDuration(100)  # Adjust the duration as needed

        # Create a sequential animation group for coordinated animations
        self.animation_group = QParallelAnimationGroup()
        self.animation_group.addAnimation(self.animation)
        self.animation_group.addAnimation(self.opacity_animation)
        self.animation_group.start()

    def get_ip(self):
        return self.ip
    
    def save_ip_address(self, ip_address_str):
        with open('last_ip.json', 'w') as f:
            json.dump(ip_address_str, f)
        