# simulator_interface.py
import numpy as np
from typing import Dict, List, Tuple, Optional

class SimulatorInterface:
    """Interface between UI and BeamformingSimulator"""
    
    def __init__(self, simulator):
        self.simulator = simulator
        self.current_array_id = 0
        self.array_units = {}  # Store multiple array configurations
        
    def add_array_unit(self, params: Dict) -> int:
        """Add a new array unit with given parameters"""
        try:
            array_id = self.current_array_id
            self.array_units[array_id] = params
            self.current_array_id += 1
            return array_id
        except Exception as e:
            raise ValueError(f"Error adding array unit: {e}")

    def update_array_geometry(self, array_id: int, params: Dict) -> bool:
        """Update array geometry with error checking"""
        try:
            # Validate parameters
            if params['n_elements'] < 2:
                raise ValueError("Must have at least 2 elements")
            if params['spacing'] <= 0:
                raise ValueError("Spacing must be positive")
            if params['array_type'] == 'Curved' and params['radius'] <= 0:
                raise ValueError("Radius must be positive")
                
            # Update simulator
            self.simulator.update_array_geometry(**params)
            
            # Store updated parameters
            self.array_units[array_id] = params
            return True
            
        except Exception as e:
            print(f"Error updating array geometry: {e}")
            return False

    def calculate_field_map(self, x_range: Tuple[float, float], 
                          y_range: Tuple[float, float], 
                          resolution: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """Calculate field map with progress reporting"""
        try:
            x = np.linspace(x_range[0], x_range[1], resolution)
            y = np.linspace(y_range[0], y_range[1], resolution)
            X, Y = np.meshgrid(x, y)
            field = np.zeros((resolution, resolution), dtype=complex)
            
            # Calculate field values
            for i in range(resolution):
                for j in range(resolution):
                    field[i,j] = self.simulator.compute_field(X[i,j], Y[i,j])
                    
            return field, (X, Y)
            
        except Exception as e:
            print(f"Error calculating field map: {e}")
            return None, None

    def calculate_radiation_pattern(self, angles: np.ndarray, 
                                 radius: float = 5.0) -> np.ndarray:
        """Calculate radiation pattern at given angles"""
        try:
            field_values = []
            for angle in angles:
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                field_values.append(self.simulator.compute_field(x, y))
            return np.array(field_values)
            
        except Exception as e:
            print(f"Error calculating radiation pattern: {e}")
            return None

    def update_beam_parameters(self, frequency: float, 
                             steering_angle: float, 
                             focus_distance: float) -> bool:
        """Update beam steering parameters"""
        try:
            self.simulator.frequency = frequency
            self.simulator.steering_angle = steering_angle
            self.simulator.focus_distance = focus_distance
            return True
            
        except Exception as e:
            print(f"Error updating beam parameters: {e}")
            return False

    def get_element_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """Get element positions and phases"""
        try:
            positions = np.array(self.simulator.elements)
            phases = self.simulator.calculate_phases(self.simulator.steering_angle)
            return positions, phases
            
        except Exception as e:
            print(f"Error getting element data: {e}")
            return None, None

    def validate_parameters(self, params: Dict) -> Tuple[bool, str]:
        """Validate array parameters"""
        try:
            # Check required parameters
            required = ['array_type', 'n_elements', 'spacing']
            if not all(key in params for key in required):
                return False, "Missing required parameters"
                
            # Validate values
            if params['n_elements'] < 2:
                return False, "Number of elements must be at least 2"
            if params['spacing'] <= 0:
                return False, "Spacing must be positive"
                
            # Validate curved array parameters
            if params['array_type'] == 'Curved':
                if 'radius' not in params or params['radius'] <= 0:
                    return False, "Invalid radius for curved array"
                if 'arc_angle' not in params:
                    return False, "Missing arc angle for curved array"
                    
            return True, "Parameters valid"
            
        except Exception as e:
            return False, str(e)

    def compute_performance_metrics(self) -> Dict:
        """Calculate array performance metrics"""
        try:
            # Get radiation pattern
            angles = np.linspace(0, 2*np.pi, 360)
            pattern = self.calculate_radiation_pattern(angles)
            
            # Calculate metrics
            pattern_db = 20 * np.log10(np.abs(pattern))
            max_idx = np.argmax(pattern_db)
            
            metrics = {
                'main_lobe_angle': np.degrees(angles[max_idx]),
                'main_lobe_magnitude': pattern_db[max_idx],
                'beam_width': self._calculate_beam_width(pattern_db, angles),
                'side_lobe_level': self._calculate_sll(pattern_db, max_idx),
            }
            
            return metrics
            
        except Exception as e:
            print(f"Error computing metrics: {e}")
            return None

    def _calculate_beam_width(self, pattern_db: np.ndarray, 
                            angles: np.ndarray) -> float:
        """Calculate 3dB beam width"""
        try:
            max_val = np.max(pattern_db)
            threshold = max_val - 3
            
            # Find points where pattern crosses threshold
            crossings = np.where(pattern_db >= threshold)[0]
            if len(crossings) >= 2:
                width = np.abs(angles[crossings[-1]] - angles[crossings[0]])
                return np.degrees(width)
            return None
            
        except Exception as e:
            print(f"Error calculating beam width: {e}")
            return None

    def _calculate_sll(self, pattern_db: np.ndarray, 
                      main_lobe_idx: int) -> float:
        """Calculate side lobe level in dB"""
        try:
            # Exclude main lobe region
            pattern_no_main = np.concatenate([
                pattern_db[:main_lobe_idx-10],
                pattern_db[main_lobe_idx+10:]
            ])
            
            if len(pattern_no_main) > 0:
                return np.max(pattern_no_main)
            return None
            
        except Exception as e:
            print(f"Error calculating side lobe level: {e}")
            return None