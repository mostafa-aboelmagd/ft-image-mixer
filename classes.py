from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QEvent, pyqtSignal
import cv2
import numpy as np

class InputWindow(QtWidgets.QLabel):
    isBrowsed = pyqtSignal(str)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.browsed = None
        self.height = 0
        self.width = 0
        self.image = None
        self.last_window_state = self.window().windowState()
        self.mouseDoubleClickEvent = self.browseImage
        
    def browseImage(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, directory='"D:\FT-Magnitude-Phase-Mixer"',filter= 'Images (*.png *.xpm *.jpg *.jpeg *.bmp *.tiff)', options=options)
        if file_path:
            cv_image = cv2.imread(file_path)
            self.browsed = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            self.height, self.width = self.browsed.shape
            self.addImage()
            self.isBrowsed.emit(file_path)
    
    def addImage(self):
        img = cv2.resize(self.browsed, (self.width, self.height))
        q_image = QImage(img.data, self.width, self.height, self.width, QImage.Format_Grayscale8)

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