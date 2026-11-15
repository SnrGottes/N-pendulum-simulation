from PyQt6.QtWidgets import (
    QWidget, QLabel, QDoubleSpinBox,
    QHBoxLayout
)

# Custom Sub-Widget for Retrieving Data
class DataSpinBox(QDoubleSpinBox):
    def __init__(self, values_data: dict, parent=None):
        super().__init__(parent)
        self.setRange(values_data['min_value'], values_data['max_value'])
        self.setValue(values_data['value'])
        self.setSingleStep(values_data['step'])
        self.setObjectName('data_spin_box')

# Custom Label Sub-Widget
class Label(QLabel):
    def __init__(self, text: str = '', parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setObjectName('label')
        
# A custom widget for retrieving and displaying data
class DataWidget(QWidget):
    def __init__(self, data: dict, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.title = Label(data['title'])
        self.title.setToolTip(data['tool_tip'])

        self.data_spin_box = DataSpinBox(data['values'])

        self.unit_label = Label(data['unit'])

        layout.addWidget(self.title)
        layout.addWidget(self.data_spin_box)
        layout.addWidget(self.unit_label)

        
        self.setLayout(layout)