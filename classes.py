from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QEvent
import cv2
import numpy as np

class InputWindow(QtWidgets.QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.image = None
        self.last_window_state = self.window().windowState()
        self.mouseDoubleClickEvent = self.browseImage
        #self.resizeEvent = self.updateScaledImage
        
    def browseImage(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, directory='"D:\FT-Magnitude-Phase-Mixer"',filter= 'Images (*.png *.xpm *.jpg *.jpeg *.bmp *.tiff)', options=options)
        if file_path:
           cv_image = cv2.imread(file_path)
           cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
           height, width = cv_image_rgb.shape
           q_image = QImage(cv_image_rgb.data, width, height, width, QImage.Format_Grayscale8)

           self.image = QPixmap.fromImage(q_image)
           self.updateScaledImage()

    def updateScaledImage(self, event = None):
        if self.image:
            scaled_pixmap = self.image.scaled(self.size(), transformMode= Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)
    
    
     

            
            
            
            
            
            
            
            
            
            
            

class ComponentWindow(QtWidgets.QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        

class OutputWindow(QtWidgets.QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)   