from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout
)

PANEL_WIDTH = 300
PANEL_HEIGHT = 50

class ButtonsPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.panel_configuration()
        self.layout_configuration()

    def panel_configuration(self):
        self.setMinimumSize(
            PANEL_WIDTH,
            PANEL_HEIGHT
        )

    def layout_configuration(self):
        cental_widget = QWidget()
        layout = QHBoxLayout(cental_widget)

        self.setLayout(layout)