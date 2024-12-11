# plots.py
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class PlotWidgetBase:
    def __init__(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setup_plot()
        
    def setup_plot(self):
        """Override in derived classes"""
        pass
        
    def update(self, *args, **kwargs):
        """Override in derived classes"""
        pass

class BeamPatternView(PlotWidgetBase):
    def setup_plot(self):
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Beam Pattern')
        self.ax.set_xlabel('X (λ)')
        self.ax.set_ylabel('Y (λ)')

        # Initialize empty intensity map
        self.beam_map = self.ax.imshow(np.zeros((100, 100)),
                                     extent=[-10, 10, -10, 10],
                                     cmap='viridis',
                                     aspect='auto')
        
        # Add colorbar
        self.figure.colorbar(self.beam_map)

        # Plot array elements
        self.element_scatter = self.ax.scatter([], [], c='red', marker='o')

        # Enable zoom/pan
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)

    def update(self, intensities, element_positions):
        """Update beam pattern plot with error checking"""
        if len(element_positions) == 0:
            print("Warning: No elements to display")
            return

        self.beam_map.set_data(intensities)
        self.element_scatter.set_offsets(element_positions)
        self.ax.set_xlim([-10, 10])
        self.ax.set_ylim([-10, 10])
        self.canvas.draw()

    def on_click(self, event):
        if event.inaxes:
            print(f'Clicked at x={event.xdata:.2f}, y={event.ydata:.2f}')

class FieldMapView(PlotWidgetBase):
    def setup_plot(self):
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Field Map')
        self.ax.set_xlabel('X (λ)')
        self.ax.set_ylabel('Y (λ)')

        # Initialize field components
        self.field_strength = self.ax.imshow(np.zeros((100, 100)),
                                           extent=[-10, 10, -10, 10],
                                           cmap='RdYlBu',
                                           aspect='auto')
        self.phase_overlay = self.ax.imshow(np.zeros((100, 100)),
                                          extent=[-10, 10, -10, 10],
                                          cmap='hsv',
                                          alpha=0.3,
                                          aspect='auto')

        # Add colorbars
        strength_cbar = self.figure.colorbar(self.field_strength)
        strength_cbar.set_label('Field Strength (dB)')
        phase_cbar = self.figure.colorbar(self.phase_overlay)
        phase_cbar.set_label('Phase (rad)')

    def update(self, field_strength, phase_data):
        self.field_strength.set_data(field_strength)
        self.phase_overlay.set_data(phase_data)
        self.canvas.draw()

    def show_field_values(self, event):
        if event.inaxes == self.ax:
            x, y = int(event.xdata), int(event.ydata)
            if 0 <= x < 100 and 0 <= y < 100:
                strength = self.field_strength.get_array()[y, x]
                phase = self.phase_overlay.get_array()[y, x]
                self.ax.set_title(
                    f'Field Strength: {strength:.2f} dB, Phase: {phase:.2f} rad')

class PolarPlotView(PlotWidgetBase):
    def setup_plot(self):
        self.ax = self.figure.add_subplot(111, projection='polar')
        self.ax.set_title('Radiation Pattern')

        # Initialize empty polar plot
        self.polar_line, = self.ax.plot([], [], 'b-')
        self.main_lobe, = self.ax.plot([], [], 'r--', label='Main Lobe')
        self.side_lobes, = self.ax.plot([], [], 'g:', label='Side Lobes')

        # Add angle markers
        self.ax.set_xticks(np.linspace(0, 2*np.pi, 12))
        self.ax.grid(True)
        self.ax.legend()

    def update(self, angles, magnitudes):
        # Normalize magnitudes to dB scale
        magnitudes_db = 20 * np.log10(np.abs(magnitudes))
        magnitudes_db = np.maximum(magnitudes_db, -40)  # Set minimum at -40dB
        
        # Update main plot
        self.polar_line.set_data(angles, magnitudes_db)
        
        # Find main lobe
        main_lobe_idx = np.argmax(magnitudes_db)
        main_lobe_angle = angles[main_lobe_idx]
        main_lobe_mag = magnitudes_db[main_lobe_idx]
        self.main_lobe.set_data([main_lobe_angle], [main_lobe_mag])
        
        # Find side lobes (peaks above -20dB)
        peaks = np.where((magnitudes_db > -20) & 
                        (magnitudes_db < main_lobe_mag))[0]
        self.side_lobes.set_data(angles[peaks], magnitudes_db[peaks])
        
        self.canvas.draw()

    def show_angle_magnitude(self, event):
        if event.inaxes == self.ax:
            angle = np.degrees(event.xdata)
            magnitude = event.ydata
            self.ax.set_title(
                f'Angle: {angle:.1f}°, Magnitude: {magnitude:.1f} dB')

class PhaseDistributionView(PlotWidgetBase):
    def setup_plot(self):
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Phase Distribution')
        self.ax.set_xlabel('Element Number')
        self.ax.set_ylabel('Phase (degrees)')

        # Initialize empty plots
        self.phase_line, = self.ax.plot([], [], 'b-o', label='Phase')
        self.amplitude_line, = self.ax.plot([], [], 'r-o', label='Amplitude')
        self.ax.grid(True)
        self.ax.legend()

    def update(self, element_numbers, phases, amplitudes):
        """Update phase distribution plot with error checking"""
        if phases is None or len(phases) == 0:
            print("Warning: No phase data to display")
            return
            
        if amplitudes is None or len(amplitudes) == 0:
            print("Warning: No amplitude data to display")
            return

        self.phase_line.set_data(element_numbers, phases)
        self.amplitude_line.set_data(element_numbers, amplitudes)
        
        self.ax.set_xlim(-1, len(element_numbers))
        self.ax.set_ylim(min(min(phases), min(amplitudes)) - 10, 
                        max(max(phases), max(amplitudes)) + 10)
        self.canvas.draw()

    def on_element_click(self, event):
        if event.inaxes == self.ax:
            element = int(round(event.xdata))
            if 0 <= element < len(self.phase_line.get_xdata()):
                print(f'Selected element {element}')
                print(f'Phase: {self.phase_line.get_ydata()[element]:.1f}°')
                print(f'Amplitude: {self.amplitude_line.get_ydata()[element]:.2f}')