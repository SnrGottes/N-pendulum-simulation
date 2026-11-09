from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout
)

PANEL_WIDTH = 100
PANEL_HEIGHT = 150

class PendulmumSelectPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.panel_configuration()

    def panel_configuration(self):
        self.setMinimumSize(
            PANEL_WIDTH,
            PANEL_HEIGHT
        )