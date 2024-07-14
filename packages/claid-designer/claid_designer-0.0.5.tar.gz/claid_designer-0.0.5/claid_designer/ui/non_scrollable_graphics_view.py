from PyQt5.QtWidgets import QGraphicsView


class NonScrollableGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)

    def scrollContentsBy(self, dx, dy):
        print("Scroll contents by ", dx, dy)
        if(dx != 0):
            return
        # Prevent horizontal scrolling
        super().scrollContentsBy(0, dy)
