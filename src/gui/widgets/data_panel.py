from PyQt6.QtCore import Qt
from src.gui.widgets.widgets import DataWidget
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea
)

class DataPanel(QWidget):
    def __init__(self, panel_settings: dict, sim_settings: dict, pendulmum_name: str, parent=None):
        super().__init__(parent)
        # Saving Settings in self
        self.settings = panel_settings
        self.sim_settings = sim_settings
        self.pendulmum_name = pendulmum_name

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
        #
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(4, 4, 4, 4)

        #
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        outer_layout.addWidget(self.scroll_area)

        #
        self.content_widget = QWidget()
        self.scroll_area.setWidget(self.content_widget)

        self.main_layout = QVBoxLayout(self.content_widget)

    def adding_data_widgets(self):
        self.data_spin_boxes: dict = {} # Variable for storing added widgets
        # We go through the parameters and create a separate widget for each one
        for parm_name in self.sim_settings['pendulmum_parms_list']['list']:
            parm_data = self.sim_settings[parm_name]

            data_spin_box = DataWidget(
                parm_data, 
                self.sim_settings[self.pendulmum_name][parm_name]
            )
            
            self.data_spin_boxes.update({parm_name: data_spin_box})
            self.main_layout.addWidget(data_spin_box)
        
        self.main_layout.addStretch()

    def update_pendulmum(self, neu_pendulmum_name: str):
        self.pendulmum_name = neu_pendulmum_name
        self.data_spin_boxes.clear()

        while self.main_layout.count():
            item = self.main_layout.takeAt(self.main_layout.count() - 1)
            widget = item.widget()
        
        if widget is not None:
            widget.deleteLater()
        
        self.adding_data_widgets()
