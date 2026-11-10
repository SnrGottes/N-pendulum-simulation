from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout
)

PANEL_WIDTH = 300
PANEL_HEIGHT = 300

class GraphPanel(QWidget):
    def __init__(self, panel_settings: dict, parent=None):
        super().__init__(parent)
        self.panel_configuration()

    def panel_configuration(self):
        self.setMinimumSize(
            PANEL_WIDTH,
            PANEL_HEIGHT
        )