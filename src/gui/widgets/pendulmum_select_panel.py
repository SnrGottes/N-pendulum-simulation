from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QScrollArea
)
from src.gui.widgets.widgets import (
    PendulmumWidget,
    NeuPendulmumWidget
)

class PendulmumSelectPanel(QWidget):
    signal = pyqtSignal(str)

    def __init__(self, panel_settings: dict, sim_settings: dict, parent=None):
        super().__init__(parent)
        self.settings = panel_settings
        self.sim_settings = sim_settings
        self.panel_configuration()
        self.layout_configuration()
        self.adding_pendulmum_widgets()

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

    def adding_pendulmum_widgets(self):
        PROPORTION_WIDGET_HEIGHT = 7
        self.pendulmum_widgets: dict = {}
        for pendulmum_name in self.sim_settings['pendulmums_list']['list']:
            pendulmum_widget = PendulmumWidget(
                int(self.settings['height']/PROPORTION_WIDGET_HEIGHT),
                self.sim_settings[pendulmum_name]['color'],
                pendulmum_name
            )

            pendulmum_widget.pendulmum_selected_signal.connect(self.on_pendulmum_clicked)

            self.main_layout.addWidget(pendulmum_widget)
            self.pendulmum_widgets.update({pendulmum_name: pendulmum_widget})

        self.neu_pendulmum_widget = NeuPendulmumWidget(
            int(self.settings['height']/PROPORTION_WIDGET_HEIGHT)
        )

        self.main_layout.addWidget(self.neu_pendulmum_widget)
        self.main_layout.addStretch()

    def on_pendulmum_clicked(self, name: str):
        print(f"Select pendulmum: {name}")
        self.signal.emit(name)