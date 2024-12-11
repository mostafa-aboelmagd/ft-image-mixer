# controls.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
                            QPushButton, QListWidget, QComboBox, QSpinBox, 
                            QDoubleSpinBox, QFormLayout, QLabel, QRadioButton)
from PyQt6.QtCore import pyqtSignal

class ArrayControlPanel(QWidget):
    # Define signals for parameter changes
    array_changed = pyqtSignal()
    beam_changed = pyqtSignal()
    frequency_changed = pyqtSignal(float)
    steering_changed = pyqtSignal(float)
    focus_changed = pyqtSignal(float)
    phase_mode_changed = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_controls()
        self.setup_ui()
        self.connect_signals()
        self.set_default_values()

    def init_controls(self):
        """Initialize all control widgets"""
        # Array configuration controls
        self.geometry_combo = QComboBox()
        self.elements_spin = QSpinBox()
        self.spacing_spin = QDoubleSpinBox()
        self.pos_x_spin = QDoubleSpinBox()
        self.pos_y_spin = QDoubleSpinBox()
        self.rotation_spin = QDoubleSpinBox()
        self.radius_spin = QDoubleSpinBox()
        self.arc_spin = QDoubleSpinBox()

        # Beam control widgets
        self.freq_spin = QDoubleSpinBox()
        self.freq_list = QListWidget()
        self.add_freq_btn = QPushButton("Add")
        self.remove_freq_btn = QPushButton("Remove")

        # Phase control widgets
        self.manual_radio = QRadioButton("Manual Mode")
        self.auto_radio = QRadioButton("Automatic Mode")
        self.steering_spin = QDoubleSpinBox()
        self.focus_spin = QDoubleSpinBox()

        # Array management
        self.add_array_btn = QPushButton("Add New Array Unit")
        self.array_list = QListWidget()

    def setup_ui(self):
        """Create and arrange the UI layout"""
        layout = QVBoxLayout(self)
        
        # Array Management Section
        layout.addWidget(self.create_array_management())
        
        # Array Configuration Section
        layout.addWidget(self.create_array_config())
        
        # Beam Control Section
        layout.addWidget(self.create_beam_control())
        
        # Add stretch to push everything to the top
        layout.addStretch()
        
        # Set minimum width for the control panel
        self.setMinimumWidth(250)

    def create_array_management(self):
        """Create array management section"""
        group = QGroupBox("Array Management")
        layout = QVBoxLayout()
        
        layout.addWidget(self.add_array_btn)
        layout.addWidget(self.array_list)
        
        group.setLayout(layout)
        return group

    def create_array_config(self):
        """Create array configuration section"""
        group = QGroupBox("Array Configuration")
        layout = QFormLayout()
        
        # Setup array configuration controls
        self.geometry_combo.addItems(["Linear", "Curved", "Custom"])
        self.elements_spin.setRange(2, 128)
        self.spacing_spin.setRange(0.1, 10.0)
        self.pos_x_spin.setRange(-10.0, 10.0)
        self.pos_y_spin.setRange(-10.0, 10.0)
        self.rotation_spin.setRange(0, 360)
        self.radius_spin.setRange(0.1, 10.0)
        self.arc_spin.setRange(-180, 180)
        
        # Add controls to layout
        layout.addRow("Geometry:", self.geometry_combo)
        layout.addRow("Elements:", self.elements_spin)
        layout.addRow("Spacing (λ):", self.spacing_spin)
        layout.addRow("Position X:", self.pos_x_spin)
        layout.addRow("Position Y:", self.pos_y_spin)
        layout.addRow("Rotation (°):", self.rotation_spin)
        layout.addRow("Radius:", self.radius_spin)
        layout.addRow("Arc Angle:", self.arc_spin)
        
        group.setLayout(layout)
        return group

    def create_beam_control(self):
        """Create beam control section"""
        group = QGroupBox("Beam Control")
        layout = QVBoxLayout()
        
        # Frequency control
        freq_group = QGroupBox("Frequency Control")
        freq_layout = QHBoxLayout()
        
        self.freq_spin.setRange(0.1, 100.0)
        freq_layout.addWidget(self.freq_spin)
        freq_layout.addWidget(self.add_freq_btn)
        freq_layout.addWidget(self.remove_freq_btn)
        
        freq_group.setLayout(freq_layout)
        layout.addWidget(freq_group)
        layout.addWidget(self.freq_list)
        
        # Phase control
        phase_group = QGroupBox("Phase Control")
        phase_layout = QVBoxLayout()
        
        self.steering_spin.setRange(-90, 90)
        self.focus_spin.setRange(0.1, 1000.0)
        
        phase_layout.addWidget(self.manual_radio)
        phase_layout.addWidget(self.auto_radio)
        phase_layout.addWidget(QLabel("Steering Angle (°):"))
        phase_layout.addWidget(self.steering_spin)
        phase_layout.addWidget(QLabel("Focus Distance:"))
        phase_layout.addWidget(self.focus_spin)
        
        phase_group.setLayout(phase_layout)
        layout.addWidget(phase_group)
        
        group.setLayout(layout)
        return group

    def connect_signals(self):
        """Connect all control signals"""
        # Array configuration signals
        self.geometry_combo.currentTextChanged.connect(self.array_changed.emit)
        self.elements_spin.valueChanged.connect(self.array_changed.emit)
        self.spacing_spin.valueChanged.connect(self.array_changed.emit)
        self.pos_x_spin.valueChanged.connect(self.array_changed.emit)
        self.pos_y_spin.valueChanged.connect(self.array_changed.emit)
        self.rotation_spin.valueChanged.connect(self.array_changed.emit)
        self.radius_spin.valueChanged.connect(self.array_changed.emit)
        self.arc_spin.valueChanged.connect(self.array_changed.emit)
        
        # Beam control signals
        self.freq_spin.valueChanged.connect(self.frequency_changed.emit)
        self.steering_spin.valueChanged.connect(self.steering_changed.emit)
        self.focus_spin.valueChanged.connect(self.focus_changed.emit)
        
        # Phase control signals
        self.manual_radio.toggled.connect(self.phase_mode_changed.emit)
        
        # Frequency list signals
        self.add_freq_btn.clicked.connect(self.add_frequency)
        self.remove_freq_btn.clicked.connect(self.remove_frequency)

    def set_default_values(self):
        """Set default values for all controls"""
        self.geometry_combo.setCurrentText("Linear")
        self.elements_spin.setValue(8)
        self.spacing_spin.setValue(0.5)
        self.pos_x_spin.setValue(0.0)
        self.pos_y_spin.setValue(0.0)
        self.rotation_spin.setValue(0.0)
        self.radius_spin.setValue(1.0)
        self.arc_spin.setValue(90.0)
        
        self.freq_spin.setValue(2.4)
        self.steering_spin.setValue(0.0)
        self.focus_spin.setValue(float('inf'))
        
        self.auto_radio.setChecked(True)

    def add_frequency(self):
        """Add current frequency to list"""
        freq = self.freq_spin.value()
        self.freq_list.addItem(f"{freq} GHz")
        self.frequency_changed.emit(freq)

    def remove_frequency(self):
        """Remove selected frequency from list"""
        current = self.freq_list.currentRow()
        if current >= 0:
            self.freq_list.takeItem(current)
            if self.freq_list.count() > 0:
                self.freq_list.setCurrentRow(0)
                text = self.freq_list.currentItem().text()
                freq = float(text.split()[0])
                self.frequency_changed.emit(freq)

    def get_array_parameters(self):
        """Get current array parameters as dictionary"""
        return {
            'array_type': self.geometry_combo.currentText(),
            'n_elements': self.elements_spin.value(),
            'spacing': self.spacing_spin.value(),
            'pos_x': self.pos_x_spin.value(),
            'pos_y': self.pos_y_spin.value(),
            'rotation': self.rotation_spin.value(),
            'radius': self.radius_spin.value(),
            'arc_angle': self.arc_spin.value()
        }

    def get_beam_parameters(self):
        """Get current beam parameters as dictionary"""
        return {
            'frequency': self.freq_spin.value(),
            'steering_angle': self.steering_spin.value(),
            'focus_distance': self.focus_spin.value(),
            'manual_mode': self.manual_radio.isChecked()
        }