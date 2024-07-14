from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QRect

class AnimatedButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        # Set dimensions
        self.defaultSize = None
        self.defaultPos = None
        self.growth = None

        # Create shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

        # Create animation
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(30)  # Animation duration in milliseconds

    def enterEvent(self, event):
        super().enterEvent(event)
        # Set the default size and position at the first hover event
        if self.defaultSize == None:
            self.defaultSize = self.size()
        if self.defaultPos == None:
            self.defaultPos = self.pos()
        if self.growth == None:
            self.growth = self.width() * 0.02
        # Animate the button
        self.animation.stop()
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(self.defaultPos.x() - self.growth/2, self.defaultPos.y() - self.growth/2, \
                                        self.width() + self.growth, self.height() + self.growth))
        self.animation.start()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        # Animate the button
        self.animation.stop()
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(self.defaultPos, self.defaultSize))
        self.animation.start()

