from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QHBoxLayout, QVBoxLayout, QSplitter,
    QWidget, QScrollArea
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_configuration() # Main window settings
        self.panels_connect()       # Connecting and creating custom panels
        self.layout_configuration() # Window layout and filling

    def window_configuration(self):
        # Saving settings in self
        from src.config_loader import ConfigLoader
        self.gui_settings = ConfigLoader.get_gui_settings()
        self.sim_settings = ConfigLoader.get_sim_settings()

        self.setMinimumSize(
            self.gui_settings['main_window']['width'],
            self.gui_settings['main_window']['height']
        )
        self.setWindowTitle(self.gui_settings['main_window']['title'])

    def panels_connect(self):
        # Import custom panel widgets
        from src.gui.widgets.buttons_panel import ButtonsPanel
        from src.gui.widgets.graph_panel import GraphPanel
        from src.gui.widgets.pendulmum_select_panel import PendulmumSelectPanel
        from src.gui.widgets.data_panel import DataPanel

        # Creating Custom Panels
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
        # Creating and Configuring the Main Window Layout
        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.setChildrenCollapsible(False)

        # Adding Panels to the Main Layout
        splitter.addWidget(self.ButtonsPanel)
        splitter.addWidget(self.GraphPanel)

        # Creating and Configuring an Additional Layout
        sub_splitter = QSplitter(Qt.Orientation.Horizontal)
        sub_splitter.setChildrenCollapsible(False)

        # Creating and configuring the scroll area required for scrolling the pendulmum select panel
        pendulmum_sroll_area = QScrollArea()
        pendulmum_sroll_area.setWidgetResizable(True)

        pendulmum_sroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        pendulmum_sroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        pendulmum_sroll_area.setWidget(self.PendulmumSelectPanel)

        # Creating and configuring the scroll area required for scrolling the data panel
        data_sroll_area = QScrollArea()
        data_sroll_area.setWidgetResizable(True)

        data_sroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        data_sroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        data_sroll_area.setWidget(self.DataPanel)

        # Adding the remaining widgets and finalizing the main layout 
        sub_splitter.addWidget(pendulmum_sroll_area)
        sub_splitter.addWidget(data_sroll_area)

        splitter.addWidget(sub_splitter)

        self.setCentralWidget(splitter)