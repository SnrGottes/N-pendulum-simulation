from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout
)

class GraphPanel(QWidget):
    def __init__(self, panel_settings: dict, parent=None):
        super().__init__(parent)
        self.settings = panel_settings
        self.panel_configuration()

    def panel_configuration(self):
        self.setMinimumSize(
            self.settings['width'],
            self.settings['height']
        )