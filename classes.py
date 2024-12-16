from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QEvent, pyqtSignal
import cv2
import numpy as np

class InputWindow(QtWidgets.QLabel):
    isBrowsed = pyqtSignal(str)
    imageUpdatedSignal = pyqtSignal()
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupVariables()
        self.addEventListeners()
    
    def setupVariables(self):
        self.setFixedSize(300, 300)
        self.uploaded = False
        self.originalBrowsed = None
        self.browsed = None
        self.q_image = None
        self.image = None
        self.width = 300
        self.height = 300
        self.last_window_state = self.window().windowState()
        self.mousePressed = False
        self.initialX = 0 # Needed for controlling the brightness and contrast of our image
        self.initialY = 0
        self.currentBrightness = 0.0
        self.currentContrast = 1.0
    
    def addEventListeners(self):
        self.mouseDoubleClickEvent = self.browseImage
        self.mousePressEvent = self.handleMousePress
        self.mouseMoveEvent = self.handleMouseMovement
        self.mouseReleaseEvent = self.handleMouseRelease
        
    def browseImage(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, directory='"D:\FT-Magnitude-Phase-Mixer"',filter= 'Images (*.png *.xpm *.jpg *.jpeg *.bmp *.tiff)', options=options)
        if file_path:
            cv_image = cv2.imread(file_path)
            self.originalBrowsed = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            self.browsed = np.copy(self.originalBrowsed)
            self.addImage()
            self.updateScaledImage()
            self.isBrowsed.emit(file_path)
            self.uploaded = True
    
    def addImage(self):
        img = cv2.resize(self.browsed, (self.width, self.height))
        self.q_image = QImage(img.data, self.width, self.height, self.width, QImage.Format_Grayscale8)
        self.image = QPixmap.fromImage(self.q_image)

    def updateScaledImage(self, event = None):
        if self.image:
            self.clear()
            scaled_pixmap = self.image.scaled(self.size(), transformMode= Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)         
            self.imageUpdatedSignal.emit()

    def handleMousePress(self, event):
        if self.uploaded:
            if event.button() == Qt.LeftButton:
                self.mousePressed = True
                self.initialX = event.x()
                self.initialY = event.y()
    
    def handleMouseMovement(self, event):
        if self.mousePressed:
            horizontalMovement = event.x() - self.initialX
            verticalMovement = event.y() - self.initialY

            self.currentBrightness = np.clip(self.currentBrightness + horizontalMovement // 10, -50, 200) # Limits the brightness values between -50 and 200
            self.currentContrast = np.clip(self.currentContrast + (verticalMovement // 100) * 0.1, 0.5, 2.0) # Multiplying by 0.1 prevents drastic contrast shifts

            newImage = cv2.convertScaleAbs(self.originalBrowsed, alpha=self.currentContrast, beta=self.currentBrightness) # alpha scales the pixel values, while beta adds an offset
            newImage = np.clip(newImage, 0, 255) # Ensures that all pixel values are clipped to this valid range
            self.browsed = newImage
            self.addImage()
            self.updateScaledImage()
            self.initialX = event.x()
            self.initialY = event.y()

    def handleMouseRelease(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePressed = False    

class ComponentWindow(QtWidgets.QLabel):
    spectrumUpdatedSignal = pyqtSignal()
    
    def __init__(self, input_window_instance, mode_combo_box, parent = None):
        super().__init__(parent)
        self.setFixedSize(300, 300)
        self.original_window_instance = input_window_instance
        self.mode_combo_box = mode_combo_box
        self.component_image = None
        self.original_window_instance.imageUpdatedSignal.connect(self.showFreqComponents)

        self.mode_combo_box.currentIndexChanged.connect(self.showFreqComponents)
    
    def showFreqComponents(self):
        if self.original_window_instance.image:
            # changing the pixmap to a 2d array (image height, image width) to compute its fourier components
           
            original_q_image = self.original_window_instance.q_image
            width = self.original_window_instance.width  # width and height are used in forming the shape(dimensions) of the formed array
            height = self.original_window_instance.height 
            ptr = original_q_image.bits()
            ptr.setsize(width * height)
            self.original_img_array = np.frombuffer(ptr, np.uint8).reshape((height, width)) # 2d array representing the img to compute its fourier transform
            
            self.freq_components = np.fft.fft2(self.original_img_array)
            self.shifted_freq_components = np.fft.fftshift(self.freq_components) # shifting frequencies to get the low frequencies in the middle
            
            magnitude_spectrum = np.log(np.abs(self.shifted_freq_components) + 1) # calculating magnitude spectrum
            magnitude_normalized = cv2.normalize(
                magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX
            ).astype(np.uint8)
            
            phase_spectrum = np.angle(self.shifted_freq_components)   # calculating phase spectrum
            phase_normalized = cv2.normalize(phase_spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            if self.mode_combo_box.currentText() == "FT Magnitude":
                height, width = magnitude_normalized.shape
                freq_q_image = QImage(magnitude_normalized.data, width, height, width, QImage.Format_Grayscale8 )
            else:
                height, width = phase_normalized.shape
                freq_q_image = QImage(phase_normalized.data, width, height, width, QImage.Format_Grayscale8)
                
            
            freq_spectrum_pixmap = QPixmap.fromImage(freq_q_image)  
            freq_spectrum_scaled_pixmap = freq_spectrum_pixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation) # scaling the freq spectrum img(after changing to pixmap) to be equal to the label size
 
            self.setPixmap(freq_spectrum_scaled_pixmap) 
            self.spectrumUpdatedSignal.emit()
            
            
class OutputWindow(QtWidgets.QLabel):
    def __init__(self, component_instance1, component_instance2, component_instance3, component_instance4, parent = None):
        super().__init__(parent)   
        self.setFixedSize(300, 300)
        self.component_instance1 = component_instance1
        self.component_instance2 = component_instance2
        self.component_instance3 = component_instance3
        self.component_instance4 = component_instance4
        
        self.component_instance1.spectrumUpdatedSignal.connect(self.showReconstructedImage)
        
    def showReconstructedImage(self):
        reconstructed_img_array = np.real(np.fft.ifft2(self.component_instance1.freq_components))
        #reconstructed_components = self.component_instance1.magnitude_spectrum * np.ex
        reconstructed_img_normalized_array = cv2.normalize(reconstructed_img_array, None, 0, 255,  cv2.NORM_MINMAX).astype(np.uint8)
        height, width = reconstructed_img_normalized_array.shape
        reconstructed_q_image = QImage(reconstructed_img_normalized_array.data, width, height, width, QImage.Format_Grayscale8 )
        output_pixmap = QPixmap.fromImage(reconstructed_q_image)
        output_scaled_pixmap = output_pixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation)
 
        self.setPixmap(output_scaled_pixmap)
        
        #print(f"diff bet original and reconstructed: {(np.abs(self.component_instance1.original_img_array - reconstructed_img_array))}")