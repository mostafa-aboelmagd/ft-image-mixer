# main.py
import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from beamforming_simulator import BeamformingSimulator
from simulator_interface import SimulatorInterface
from controls import ArrayControlPanel
from plots import (BeamPatternView, FieldMapView, 
                  PolarPlotView, PhaseDistributionView)

class BeamformerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Beamformer Analysis')
        self.setMinimumSize(800, 800)
        
        # Initialize simulator and interface
        self.simulator = BeamformingSimulator()
        self.sim_interface = SimulatorInterface(self.simulator)
        
        # Setup UI components
        self.setup_ui()
        self.connect_signals()
        
    def setup_ui(self):
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Create control panel (left sidebar)
        self.control_panel = ArrayControlPanel()
        self.control_panel.setMinimumWidth(250)
        main_layout.addWidget(self.control_panel)
        
        # Create plots container
        plots_container = QWidget()
        plots_layout = QVBoxLayout(plots_container)
        plots_layout.setSpacing(10)  # Add spacing between rows
        
        # Create plot views
        self.beam_view = BeamPatternView()      # TOP LEFT
        self.field_view = FieldMapView()        # TOP RIGHT
        self.polar_view = PolarPlotView()       # BOTTOM LEFT
        self.phase_view = PhaseDistributionView() # BOTTOM RIGHT
        
        # Create top row of plots (Beam Pattern and Field Map)
        top_row = QHBoxLayout()
        top_row.setSpacing(10)  # Add spacing between plots
        top_row.addWidget(self.beam_view.canvas)    # TOP LEFT
        top_row.addWidget(self.field_view.canvas)   # TOP RIGHT
        
        # Create bottom row of plots (Polar Plot and Phase Plot)
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)  # Add spacing between plots
        bottom_row.addWidget(self.polar_view.canvas)  # BOTTOM LEFT
        bottom_row.addWidget(self.phase_view.canvas)  # BOTTOM RIGHT
        
        # Add rows to plots layout with equal stretch
        plots_layout.addLayout(top_row, stretch=1)
        plots_layout.addLayout(bottom_row, stretch=1)
        
        # Add plots container to main layout
        main_layout.addWidget(plots_container, stretch=2)
        
        # Set size ratios
        main_layout.setStretch(0, 1)  # Control panel takes 1 part
        main_layout.setStretch(1, 3)  # Plots take 3 parts
        
        # Set minimum size for main window
        self.setMinimumSize(1200, 800)

    def connect_signals(self):
        # Connect control panel signals
        self.control_panel.array_changed.connect(self.update_array)
        self.control_panel.frequency_changed.connect(self.update_frequency)
        self.control_panel.steering_changed.connect(self.update_steering)
        self.control_panel.focus_changed.connect(self.update_focus)
        self.control_panel.phase_mode_changed.connect(self.update_phase_mode)

    def update_array(self):
        """Update array configuration"""
        params = self.control_panel.get_array_parameters()
        if self.sim_interface.update_array_geometry(0, params):
            self.update_plots()

    def update_frequency(self, value):
        """Update operating frequency"""
        beam_params = self.control_panel.get_beam_parameters()
        self.sim_interface.update_beam_parameters(
            frequency=value * 1e9,  # Convert GHz to Hz
            steering_angle=beam_params['steering_angle'],
            focus_distance=beam_params['focus_distance']
        )
        self.update_plots()

    def update_steering(self, value):
        """Update steering angle"""
        beam_params = self.control_panel.get_beam_parameters()
        self.sim_interface.update_beam_parameters(
            frequency=beam_params['frequency'] * 1e9,
            steering_angle=value,
            focus_distance=beam_params['focus_distance']
        )
        self.update_plots()

    def update_focus(self, value):
        """Update focus distance"""
        beam_params = self.control_panel.get_beam_parameters()
        self.sim_interface.update_beam_parameters(
            frequency=beam_params['frequency'] * 1e9,
            steering_angle=beam_params['steering_angle'],
            focus_distance=value
        )
        self.update_plots()

    def update_phase_mode(self, manual_mode):
        """Update phase control mode"""
        # Update UI elements based on mode
        self.control_panel.steering_spin.setEnabled(not manual_mode)
        self.control_panel.focus_spin.setEnabled(not manual_mode)
        self.update_plots()

    def update_plots(self):
        """Update all visualization plots"""
        try:
            # Get field map
            field, (X, Y) = self.sim_interface.calculate_field_map(
                x_range=(-5, 5),
                y_range=(-5, 5)
            )
            
            if field is not None:
                # Get element data
                positions, phases = self.sim_interface.get_element_data()
                
                # Calculate radiation pattern
                angles = np.linspace(0, 2*np.pi, 360)
                pattern = self.sim_interface.calculate_radiation_pattern(angles)
                
                # Update plots
                intensity = np.abs(field)**2
                self.beam_view.update(intensity, positions)
                self.field_view.update(20*np.log10(np.abs(field)), np.angle(field))
                self.polar_view.update(angles, pattern)
                self.phase_view.update(
                    np.arange(len(positions)), 
                    phases * 180/np.pi, 
                    np.ones_like(phases)
                )
                
        except Exception as e:
            print(f"Error updating plots: {e}")

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = BeamformerUI()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Application error: {e}")