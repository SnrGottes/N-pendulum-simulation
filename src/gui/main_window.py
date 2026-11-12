from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QHBoxLayout, QVBoxLayout, 
    QWidget, QScrollArea
)

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 500
WINDOW_TITLE = ''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_configuration()
        self.panels_connect()
        self.layout_configuration()

    def window_configuration(self):
        from src.config_loader import ConfigLoader
        self.gui_settings = ConfigLoader.get_gui_settings()
        self.sim_settings = ConfigLoader.get_sim_settings()

        self.setMinimumSize(
            self.gui_settings['main_window']['width'],
            self.gui_settings['main_window']['height']
        )
        self.setWindowTitle(self.gui_settings['main_window']['title'])

    def panels_connect(self):
        from src.gui.widgets.buttons_panel import ButtonsPanel
        from src.gui.widgets.graph_panel import GraphPanel
        from src.gui.widgets.pendulmum_select_panel import PendulmumSelectPanel
        from src.gui.widgets.data_panel import DataPanel

        self.ButtonsPanel = ButtonsPanel(
            self.gui_settings['panels']['buttons_panel']
        )
        self.GraphPanel = GraphPanel(
            self.gui_settings['panels']['graph_panel']
        )
        self.PendulmumSelectPanel = PendulmumSelectPanel(
            self.gui_settings['panels']['pendulmum_select_panel']
        )
        self.DataPanel = DataPanel(
            self.gui_settings['panels']['data_panel'],
            self.sim_settings
        )

    def layout_configuration(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.ButtonsPanel)
        layout.addWidget(self.GraphPanel)

        sub_layout = QHBoxLayout()
        sub_layout.setSpacing(0)
        sub_layout.setContentsMargins(0, 0, 0, 0)

        data_sroll_area = QScrollArea()
        data_sroll_area.setWidgetResizable(True)

        data_sroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        data_sroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        data_sroll_area.setWidget(self.DataPanel)

        sub_layout.addWidget(self.PendulmumSelectPanel)
        sub_layout.addWidget(data_sroll_area)

        layout.addLayout(sub_layout)

        self.setCentralWidget(central_widget)