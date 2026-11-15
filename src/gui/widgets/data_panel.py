from PyQt6.QtCore import Qt
from src.gui.widgets.widgets import DataWidget
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout
)

class DataPanel(QWidget):
    def __init__(self, panel_settings: dict, sim_settings: dict, parent=None):
        super().__init__(parent)
        # Saving Settings in self
        self.settings = panel_settings
        self.sim_settings = sim_settings

        self.panel_configuration()  # Main Widget Settings
        self.layout_configuration() # Creating and Configuring the Main Layout
        self.adding_data_widgets()  # Creating and Configuring Data-Handling Widgets

    def panel_configuration(self):
        self.setMinimumSize(
            self.settings['width'],
            self.settings['height']
        )
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setObjectName("Panel")

    def layout_configuration(self):
        self.main_layout = QVBoxLayout()

        self.setLayout(self.main_layout)

    def adding_data_widgets(self):
        self.data_spin_boxes: dict = {} # Variable for storing added widgets
        # We go through the parameters and create a separate widget for each one
        for parm_name in self.sim_settings['pendulmum_parms_list']['list']:
            parm_data = self.sim_settings[parm_name]
            data_spin_box = DataWidget(parm_data)
            self.data_spin_boxes.update({parm_name: data_spin_box})
            self.main_layout.addWidget(data_spin_box)
        
        self.main_layout.addStretch()
            
