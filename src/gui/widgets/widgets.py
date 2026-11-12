from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel, QScrollArea, QDoubleSpinBox,
    QVBoxLayout, QHBoxLayout, QGridLayout
)

class DataSpinBox(QDoubleSpinBox):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)
        self.setRange(data['min_value'], data['max_value'])
        self.setValue(data['value'])
        self.setSingleStep(data['step'])
        self.setObjectName('data_spin_box')

class Label(QLabel):
    def __init__(self, text: str = '', parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setObjectName('label')
        

class DataWidget(QWidget):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.title = Label(data['title'])
        self.title.setToolTip(data['tool_tip'])

        self.data_spin_box = DataSpinBox(data['values'])

        self.unit_label = Label(data['unit'])

        layout.addWidget(self.title, 0, 0, 1, 3)
        layout.addWidget(self.data_spin_box, 0, 1, 1, 2)
        layout.addWidget(self.unit_label, 0, 2, 1, 1)

        
        self.setLayout(layout)