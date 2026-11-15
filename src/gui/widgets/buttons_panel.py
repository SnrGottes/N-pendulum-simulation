from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout
)
from src.gui.widgets.widgets import Button

class ButtonsPanel(QWidget):
    def __init__(self, panel_settings: dict, parent=None):
        super().__init__(parent)
        self.settings = panel_settings
        self.panel_configuration()  #
        self.layout_configuration() #
        self.widget_filling()       # Filling out the widget

    def panel_configuration(self):
        self.setMinimumSize(
            self.settings['width'],
            self.settings['height']
        )
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("Panel")

        self.started = False
        self.paused = False

    def layout_configuration(self):
        self.main_layout = QHBoxLayout()

        self.setLayout(self.main_layout)

    def widget_filling(self):
        self.settings_button = Button('settings')
        self.plots_button = Button('plots')
        self.pause_button = Button('pause')
        self.start_button = Button('start')

        self.main_layout.addWidget(self.settings_button)
        self.main_layout.addWidget(self.plots_button)
        self.main_layout.addWidget(self.pause_button)
        self.main_layout.addWidget(self.start_button)

        self.settings_button.clicked.connect(self.clicked_settings)
        self.plots_button.clicked.connect(self.clicked_plots)
        self.pause_button.clicked.connect(self.clicked_pause)
        self.start_button.clicked.connect(self.clicked_start)

        self.pause_button.setEnabled(False)

    def clicked_settings(self):
        pass

    def clicked_plots(self):
        pass

    def clicked_pause(self):
        if self.paused:
            self.paused = False

            self.pause_button.setText('pause')
            self.plots_button.setEnabled(False)
        else:
            self.paused = True
            
            self.pause_button.setText('continue')
            self.plots_button.setEnabled(True)

    def clicked_start(self):
        if self.started:
            self.started = False
            self.start_button.setText('start')

            self.plots_button.setEnabled(True)
            self.pause_button.setEnabled(False)
        else:
            self.started = True
            self.start_button.setText('stop')

            self.plots_button.setEnabled(False)
            self.pause_button.setEnabled(True)