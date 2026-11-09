from PyQt6.QtWidgets import (
    QMainWindow, QHBoxLayout, QVBoxLayout, QWidget
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
        self.setMinimumSize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )
        self.setWindowTitle(WINDOW_TITLE)

    def panels_connect(self):
        from src.gui.widgets.buttons_panel import ButtonsPanel
        from src.gui.widgets.graph_panel import GraphPanel
        from src.gui.widgets.pendulmum_select_panel import PendulmumSelectPanel
        from src.gui.widgets.data_panel import DataPanel

        self.ButtonsPanel = ButtonsPanel()
        self.GraphPanel = GraphPanel()
        self.PendulmumSelectPanel = PendulmumSelectPanel()
        self.DataPanel = DataPanel()

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

        sub_layout.addWidget(self.PendulmumSelectPanel)
        sub_layout.addWidget(self.DataPanel)

        layout.addLayout(sub_layout)

        self.setCentralWidget(central_widget)