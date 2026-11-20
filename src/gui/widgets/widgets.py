from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QLabel, QDoubleSpinBox, QPushButton, QSizePolicy,
    QHBoxLayout
)

#
class Button(QPushButton):
    def __init__(self, text: str = '', parent = None):
        super().__init__(parent)
        self.setText(text)
        self.setObjectName('Button')
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

# Custom Sub-Widget for Retrieving Data
class DataSpinBox(QDoubleSpinBox):
    def __init__(self, values_data: dict, value: float, parent=None):
        super().__init__(parent)
        self.setRange(values_data['min_value'], values_data['max_value'])
        self.setValue(value)
        self.setSingleStep(values_data['step'])
        self.setObjectName('data_spin_box')

# Custom Label Sub-Widget
class Label(QLabel):
    def __init__(self, text: str = '', parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setObjectName('label')

#
class PendulmumWidget(QWidget):
    pendulmum_selected_signal = pyqtSignal(str)
    def __init__(self, height: int, color: str = '#fff', title: str = '', parent = None):
        super().__init__(parent)
        self.pendulmum_name = title

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedHeight(height)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.button = Button(self.pendulmum_name)
        self.button.setObjectName('Pendulmum_button')
        self.button.clicked.connect(self.pendulmum_selected)
        self.button.setStyleSheet(self.button.styleSheet() + f'''
            color: {color}; 
            border: 2px solid {color}
        ''')
        layout.addWidget(self.button)
        self.setLayout(layout)

    def pendulmum_selected(self):
        self.pendulmum_selected_signal.emit(self.pendulmum_name)

#
class NeuPendulmumWidget(QWidget):
    def __init__(self, height: int, parent = None):
        super().__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedHeight(height)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.button = Button('+')
        self.button.setObjectName('Pendulmum_button')
        self.button.setStyleSheet(self.button.styleSheet() + f'''
            color: #aaa; 
            border: 2px solid #aaa;
            font-weight: bold;
            font-size: 14px;
        ''')
        layout.addWidget(self.button)
        self.setLayout(layout)
        
# A custom widget for retrieving and displaying data
class DataWidget(QWidget):
    def __init__(self, data: dict, value: float, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.title = Label(data['title'])
        self.title.setToolTip(data['tool_tip'])

        self.data_spin_box = DataSpinBox(data['values'], value)

        self.unit_label = Label(data['unit'])

        layout.addWidget(self.title)
        layout.addWidget(self.data_spin_box)
        layout.addWidget(self.unit_label)

        
        self.setLayout(layout)