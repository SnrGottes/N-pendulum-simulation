from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout
)

class ButtonsPanel(QWidget):
    def __init__(self, panel_settings: dict, parent=None):
        super().__init__(parent)
        self.settings = panel_settings
        self.panel_configuration()
        self.layout_configuration()

    def panel_configuration(self):
        self.setMinimumSize(
            self.settings['width'],
            self.settings['height']
        )

    def layout_configuration(self):
        cental_widget = QWidget()
        layout = QHBoxLayout(cental_widget)

        self.setLayout(layout)