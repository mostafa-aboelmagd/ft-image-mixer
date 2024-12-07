# beamforming_simulator.py
import numpy as np

class BeamformingSimulator:
    def __init__(self):
        self.c = 3e8  # Speed of light
        self.reset()
        
    def reset(self):
        self.elements = []
        self.frequency = 2.4e9  # Default 2.4 GHz
        self.element_spacing = 0.5  # In wavelengths
        self.steering_angle = 0  # In degrees
        self.focus_distance = float('inf')
        self.array_type = 'linear'
        self.radius = 1.0
        self.arc_angle = 90
        
    def update_array_geometry(self, array_type, n_elements, spacing, pos_x=0, pos_y=0, 
                            rotation=0, radius=1.0, arc_angle=90):
        self.array_type = array_type
        self.elements = []
        wavelength = self.c / self.frequency
        
        if array_type == 'Linear':
            for i in range(n_elements):
                x = i * spacing * wavelength
                self.elements.append([x, 0])
                
        elif array_type == 'Curved':
            self.radius = radius
            self.arc_angle = arc_angle
            angles = np.linspace(-arc_angle/2, arc_angle/2, n_elements) * np.pi/180
            for angle in angles:
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                self.elements.append([x, y])
                
        # Apply position offset and rotation
        self.elements = np.array(self.elements)
        if rotation != 0:
            rot_matrix = np.array([[np.cos(rotation*np.pi/180), -np.sin(rotation*np.pi/180)],
                                 [np.sin(rotation*np.pi/180), np.cos(rotation*np.pi/180)]])
            self.elements = self.elements @ rot_matrix
        
        self.elements += np.array([pos_x, pos_y])

    # def update_array_geometry(self, array_type, n_elements, spacing, pos_x=0, pos_y=0, 
    #                     rotation=0, radius=1.0, arc_angle=90):
    #     """Update array geometry with error checking"""
    #     if n_elements < 2:
    #         raise ValueError("Must have at least 2 elements")
    #     if spacing <= 0:
    #         raise ValueError("Spacing must be positive")
            
    #     self.array_type = array_type
    #     self.elements = []
    #     wavelength = self.c / self.frequency
        
    #     # Create elements based on array type
    #     if array_type == 'Linear':
    #         self.elements = [[i * spacing * wavelength, 0] for i in range(n_elements)]
            
    #     elif array_type == 'Curved':
    #         if radius <= 0:
    #             raise ValueError("Radius must be positive")
    #         self.radius = radius
    #         self.arc_angle = arc_angle
    #         angles = np.linspace(-arc_angle/2, arc_angle/2, n_elements) * np.pi/180
    #         self.elements = [[radius * np.cos(angle), radius * np.sin(angle)] 
    #                         for angle in angles]
        
    #     # Convert to numpy array for operations
    #     self.elements = np.array(self.elements)
        
    #     # Apply rotation if needed
    #     if rotation != 0:
    #         rot_matrix = np.array([[np.cos(rotation*np.pi/180), -np.sin(rotation*np.pi/180)],
    #                             [np.sin(rotation*np.pi/180), np.cos(rotation*np.pi/180)]])
    #         self.elements = self.elements @ rot_matrix
        
    #     # Apply position offset
    #     self.elements += np.array([pos_x, pos_y])   
    
    # def update_array_geometry(self, array_type, n_elements, spacing, pos_x=0, pos_y=0, 
    #                     rotation=0, radius=1.0, arc_angle=90):
    #     """Update array geometry with error checking"""
    #     if n_elements < 2:
    #         raise ValueError("Must have at least 2 elements")
    #     if spacing <= 0:
    #         raise ValueError("Spacing must be positive")
            
    #     self.array_type = array_type
    #     wavelength = self.c / self.frequency
        
    #     # Create elements based on array type
    #     if array_type == 'Linear':
    #         self.elements = np.array([[i * spacing * wavelength, 0] for i in range(n_elements)])
            
    #     elif array_type == 'Curved':
    #         if radius <= 0:
    #             raise ValueError("Radius must be positive")
    #         self.radius = radius
    #         self.arc_angle = arc_angle
    #         angles = np.linspace(-arc_angle/2, arc_angle/2, n_elements) * np.pi/180
    #         self.elements = np.array([[radius * np.cos(angle), radius * np.sin(angle)] 
    #                         for angle in angles])
    #     else:
    #         raise ValueError(f"Unknown array type: {array_type}")
        
    #     # Apply rotation if needed
    #     if rotation != 0:
    #         rot_matrix = np.array([[np.cos(rotation*np.pi/180), -np.sin(rotation*np.pi/180)],
    #                             [np.sin(rotation*np.pi/180), np.cos(rotation*np.pi/180)]])
    #         self.elements = self.elements @ rot_matrix
        
    #     # Apply position offset using broadcasting
    #     if self.elements.size > 0:  # Only apply offset if elements exist
    #         offset = np.array([pos_x, pos_y])
    #         self.elements = self.elements + offset[np.newaxis, :]


    # def calculate_phases(self, steering_angle):
    #     """Calculate element phases for beam steering"""
    #     wavelength = self.c / self.frequency
    #     k = 2 * np.pi / wavelength
        
    #     if self.array_type == 'Linear':
    #         # Progressive phase shift for linear array
    #         d = self.element_spacing * wavelength
    #         phase_shift = -k * d * np.sin(steering_angle * np.pi/180)
    #         return np.arange(len(self.elements)) * phase_shift
                
    #     elif self.array_type == 'Curved':
    #         # Focus phases for curved array
    #         phases = np.zeros(len(self.elements))
            
    #         # Limit focus distance to prevent overflow
    #         focus_dist = min(self.focus_distance, 1000 * wavelength)
            
    #         focus_point = np.array([
    #             focus_dist * np.cos(steering_angle * np.pi/180),
    #             focus_dist * np.sin(steering_angle * np.pi/180)
    #         ])
            
    #         # Calculate and normalize distances
    #         distances = np.array([np.linalg.norm(focus_point - element) 
    #                             for element in self.elements])
    #         distances = distances - np.min(distances)  # Normalize to prevent overflow
            
    #         # Calculate phases
    #         phases = -k * distances
            
    #         return phases % (2 * np.pi)  # Wrap phases to [0, 2π]   
   
    def calculate_phases(self, steering_angle):
        """Calculate element phases for beam steering"""
        if len(self.elements) == 0:
            return np.array([])  # Return empty array instead of None
            
        wavelength = self.c / self.frequency
        k = 2 * np.pi / wavelength
        
        if self.array_type == 'Linear':
            d = self.element_spacing * wavelength
            phase_shift = -k * d * np.sin(steering_angle * np.pi/180)
            return np.arange(len(self.elements)) * phase_shift
                
        elif self.array_type == 'Curved':
            phases = np.zeros(len(self.elements))
            focus_point = np.array([
                self.focus_distance * np.cos(steering_angle * np.pi/180),
                self.focus_distance * np.sin(steering_angle * np.pi/180)
            ])
            
            for i, element in enumerate(self.elements):
                distance = np.linalg.norm(focus_point - element)
                phases[i] = -k * distance
            
            return phases - np.min(phases)  # Normalize phases
            
        return np.zeros(len(self.elements))  # Default case

    def compute_field(self, x, y):
        """Compute field at given point"""
        wavelength = self.c / self.frequency
        k = 2 * np.pi / wavelength
        point = np.array([x, y])
        
        # Get element phases
        phases = self.calculate_phases(self.steering_angle)
        
        # Sum contributions from all elements
        field = 0
        for i, element in enumerate(self.elements):
            r = np.linalg.norm(point - element)
            if r > 0:  # Avoid division by zero
                # Phase from element position and steering
                total_phase = k * r + phases[i]
                # 1/r amplitude decay
                field += np.exp(1j * total_phase) / np.sqrt(r)
                
        return field

