from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QEvent, pyqtSignal
import cv2
import numpy as np
_translate = QtCore.QCoreApplication.translate

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
    
    def __init__(self, input_window_instance, mode_combo_box, magPhase_radio, realImaginary_radio, parent = None):
        super().__init__(parent)
        self.setFixedSize(300, 300)
        self.original_window_instance = input_window_instance
        self.mode_combo_box = mode_combo_box  # combo box for choosing the spectrum to show in the label
        self.magPhase_radio = magPhase_radio  # mode1 radio btn
        self.realImaginary_radio = realImaginary_radio  # mode2 radio btn
        self.original_window_instance.imageUpdatedSignal.connect(self.computeFreqComponents)  # when an input image is uploaded, compute its fft
        self.freq_components = None

        self.mode_combo_box.currentIndexChanged.connect(self.selectMode) # when toggling the comboBox, go to selectMode method which leads you to showing the correct spectrum
        self.realImaginary_radio.toggled.connect(self.selectMode)  # when toggling the radio btn, go to selectMode method to choose the selected mode and show the corresponding spectrum
    
    def computeFreqComponents(self):
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
            
            # magnitude spectrum
            self.magnitude_spectrum = np.abs(self.shifted_freq_components)
            self.magnitude_logged_spectrum = np.log(self.magnitude_spectrum) # taking the log to minimize its range
            self.magnitude_normalized = cv2.normalize(
                self.magnitude_logged_spectrum, None, 0, 255, cv2.NORM_MINMAX
            ).astype(np.uint8)
            
            # phase spectrum
            self.phase_spectrum = np.angle(self.shifted_freq_components)   # calculating phase spectrum
            self.phase_normalized = cv2.normalize(self.phase_spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            # real spectrum
            self.real_spectrum = np.real(self.shifted_freq_components)
            self.real_logged_spectrum = np.log(self.real_spectrum)
            self.real_normalized = cv2.normalize(self.real_logged_spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            # imaginary spectrum
            self.imaginary_spectrum = np.imag(self.shifted_freq_components)
            self.imaginary_normalized = cv2.normalize(self.imaginary_spectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            # choosing the mode to show depending on the checked radio btn (magPhase or realImaginary)
            if not self.realImaginary_radio.isChecked(): 
                self.showMagPhaseComponent()
            else:
                self.showRealImagComponent()
    
    
    def selectMode(self):    # select 'mag and phase' mode or 'real and img' mode according to the selected radio button
        if not self.realImaginary_radio.isChecked(): 
            self.mode_combo_box.setItemText(0, _translate("MainWindow", "FT Magnitude"))
            self.mode_combo_box.setItemText(1, _translate("MainWindow", "FT Phase"))
            self.showMagPhaseComponent()
                
                
        elif self.realImaginary_radio.isChecked():
            self.mode_combo_box.setItemText(0, _translate("MainWindow", "FT Real"))
            self.mode_combo_box.setItemText(1, _translate("MainWindow", "FT Img"))
            self.showRealImagComponent()
            
            
            

    
    def showMagPhaseComponent(self):
        if self.freq_components is not None:  # if there is an image found whose fft is computed (the label isn't empty)
            if self.mode_combo_box.currentIndex() == 0:
                        height, width = self.magnitude_normalized.shape
                        freq_q_image = QImage(self.magnitude_normalized.data, width, height, width, QImage.Format_Grayscale8 )
            else:
                height, width = self.phase_normalized.shape
                freq_q_image = QImage(self.phase_normalized.data, width, height, width, QImage.Format_Grayscale8)
            freq_spectrum_pixmap = QPixmap.fromImage(freq_q_image)    #changing from qimage to pixmap
            freq_spectrum_scaled_pixmap = freq_spectrum_pixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation) # scaling the freq spectrum img(after changing to pixmap) to be equal to the label size
            self.setPixmap(freq_spectrum_scaled_pixmap)   #showing the scaled pixmap
            self.spectrumUpdatedSignal.emit()
        
        
    def showRealImagComponent(self):
        if self.freq_components is not None:
            if self.mode_combo_box.currentIndex() == 0:
                    height, width = self.real_normalized.shape
                    freq_q_image = QImage(self.real_normalized.data, width, height, width, QImage.Format_Grayscale8 )
        
            else:
                height, width = self.imaginary_normalized.shape
                freq_q_image = QImage(self.imaginary_normalized.data, width, height, width, QImage.Format_Grayscale8 )
                
            freq_spectrum_pixmap = QPixmap.fromImage(freq_q_image)  
            freq_spectrum_scaled_pixmap = freq_spectrum_pixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation) # scaling the freq spectrum img(after changing to pixmap) to be equal to the label size
            self.setPixmap(freq_spectrum_scaled_pixmap) 
            self.spectrumUpdatedSignal.emit()
            
            
            
            
class OutputWindow(QtWidgets.QLabel):
    def __init__(self, component_instance1, component_instance2, component_instance3, component_instance4, realImaginary_radio, parent = None):
        super().__init__(parent)   
        self.setFixedSize(300, 300)
        self.component_instance1 = component_instance1
        self.component_instance2 = component_instance2
        self.component_instance3 = component_instance3
        self.component_instance4 = component_instance4
        self.realImaginary_radio = realImaginary_radio
        self.output_scaled_pixmap = None
        
        
        self.component_instance1.spectrumUpdatedSignal.connect(self.showReconstructedImage)
        self.component_instance2.spectrumUpdatedSignal.connect(self.showReconstructedImage)
        self.component_instance3.spectrumUpdatedSignal.connect(self.showReconstructedImage)
        self.component_instance4.spectrumUpdatedSignal.connect(self.showReconstructedImage)
        
    def showReconstructedImage(self):
        self.total_magnitudes = np.zeros((300, 300))
        self.total_phases = np.zeros((300, 300))
        self.total_real = np.zeros((300, 300))
        self.total_imaginary = np.zeros((300, 300))
        # mixing first frequency components
        if self.component_instance1.freq_components is not None:   
            component1_magnitudes = self.component_instance1.magnitude_spectrum
            component1_phases = self.component_instance1.phase_spectrum
            component1_real = self.component_instance1.real_spectrum
            component1_imaginary = self.component_instance1.imaginary_spectrum
            self.total_magnitudes += component1_magnitudes 
            self.total_phases += component1_phases
            self.total_real += component1_real
            self.total_imaginary += component1_imaginary
        # mixing second frequency components
        if self.component_instance2.freq_components is not None:
            component2_magnitudes = self.component_instance2.magnitude_spectrum
            component2_phases = self.component_instance2.phase_spectrum
            component2_real = self.component_instance2.real_spectrum
            component2_imaginary = self.component_instance2.imaginary_spectrum
            self.total_magnitudes += component2_magnitudes 
            self.total_phases += component2_phases
            self.total_real += component2_real
            self.total_imaginary += component2_imaginary
        # mixing third frequency componenets
        if self.component_instance3.freq_components is not None:
            component3_magnitudes = self.component_instance3.magnitude_spectrum
            component3_phases = self.component_instance3.phase_spectrum
            component3_real = self.component_instance3.real_spectrum
            component3_imaginary = self.component_instance3.imaginary_spectrum
            self.total_magnitudes += component3_magnitudes 
            self.total_phases += component3_phases
            self.total_real += component3_real
            self.total_imaginary += component3_imaginary
        # mixing fourth frequency components
        if self.component_instance4.freq_components is not None:
            component4_magnitudes = self.component_instance4.magnitude_spectrum
            component4_phases = self.component_instance4.phase_spectrum
            component4_real = self.component_instance4.real_spectrum
            component4_imaginary = self.component_instance4.imaginary_spectrum
            self.total_magnitudes += component4_magnitudes 
            self.total_phases += component4_phases
            self.total_real += component4_real
            self.total_imaginary += component4_imaginary
            
        if not self.realImaginary_radio.isChecked(): 
            reconstructed_freq_components = self.total_magnitudes * np.exp(1j * self.total_phases)
            print("combining mags and phases")
        elif self.realImaginary_radio.isChecked(): 
            reconstructed_freq_components = self.total_real + 1j * self.total_imaginary
            print("combining real and imaginary")
            
        reconstructed_img_array = np.abs(np.fft.ifft2(reconstructed_freq_components))
        reconstructed_img_normalized_array = cv2.normalize(reconstructed_img_array, None, 0, 255,  cv2.NORM_MINMAX).astype(np.uint8)
        height, width = reconstructed_img_normalized_array.shape
        reconstructed_q_image = QImage(reconstructed_img_normalized_array.data, width, height, width, QImage.Format_Grayscale8 )
        output_pixmap = QPixmap.fromImage(reconstructed_q_image)
        self.output_scaled_pixmap = output_pixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation)
 
        self.setPixmap(self.output_scaled_pixmap)
        
        #print(f"diff bet original and reconstructed: {(np.abs(self.component_instance1.original_img_array - reconstructed_img_array))}")