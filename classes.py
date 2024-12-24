from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPainter
import cv2
import numpy as np
import logging
_translate = QtCore.QCoreApplication.translate

# Basic configuration for logging
logging.basicConfig(filename='app.log',  # Log messages will be written to 'app.log'
                    level=logging.DEBUG,
                    format='%(levelname)s - %(message)s')

class InputWindow(QtWidgets.QLabel):
    imageUpdatedSignal = pyqtSignal() # Determines when to compute fourier components of the browsed image
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupVariables()
        self.addEventListeners()
    
    def setupVariables(self):
        self.setFixedSize(300, 300)
        self.uploaded = False
        self.originalBrowsed = None # Browsed image in grey scale
        self.browsed = None # Copy of the original browsed which allows us to manipulate the brightness and contrast of the original grey scale image
        self.q_image = None
        self.image = None
        self.width = 300
        self.height = 300
        self.last_window_state = self.window().windowState()
        self.mousePressed = False # Needed for controlling the brightness and contrast of our image
        self.initialX = 0
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
        logging.info("Browsing Image")
        file_path, _ = QFileDialog.getOpenFileName(self, directory='"D:\FT-Magnitude-Phase-Mixer"',filter= 'Images (*.png *.xpm *.jpg *.jpeg *.bmp *.tiff)', options=options)
        if file_path:
            logging.info("Browsed Successfully")
            cvImage = cv2.imread(file_path)
            self.originalBrowsed = cv2.cvtColor(cvImage, cv2.COLOR_BGR2GRAY)
            self.browsed = np.copy(self.originalBrowsed)
            self.addImage()
            self.updateScaledImage()
            self.uploaded = True
        else:
            logging.error("Couldn't Browse Image")

    def addImage(self):
        img = cv2.resize(self.browsed, (self.width, self.height))
        self.q_image = QImage(img.data, self.width, self.height, self.width, QImage.Format_Grayscale8)
        self.image = QPixmap.fromImage(self.q_image)

    # Shows the browsed image after scaling it to fit into the UI container
    def updateScaledImage(self):
        if self.image:
            self.clear()
            scaledPixmap = self.image.scaled(self.size(), transformMode= Qt.SmoothTransformation)
            self.setPixmap(scaledPixmap)         
            self.imageUpdatedSignal.emit()

    def handleMousePress(self, event):
        if self.uploaded:
            if event.button() == Qt.LeftButton:
                logging.info("Changing Brightness & Contrast")
                self.mousePressed = True
                self.initialX = event.x()
                self.initialY = event.y()
            else:
                logging.warning("Press Left Mouse To Be Able To Change Brightness")
        else:
            logging.error("Can't Update Brightness Unless An Image Is Uploaded")
    
    # Manipulates Brightness & Contrast of image via moving the mouse horizontally and vertically respectively
    def handleMouseMovement(self, event):
        if self.mousePressed:
            verticalMovement = self.initialY - event.y()
            horizontalMovement = event.x() - self.initialX

            self.currentBrightness = np.clip(self.currentBrightness + verticalMovement // 10, -50, 200) # Limits the brightness values between -50 and 200
            self.currentContrast = np.clip(self.currentContrast + (horizontalMovement // 100) * 0.1, 0.5, 2.0) # Multiplying by 0.1 prevents major contrast shifts

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
    regionResizedSignal = pyqtSignal()

    def __init__(self, inputWindowInstance, modeComboBox, magPhaseRadio, innerRegion, parent = None):
        super().__init__(parent)
        self.setupVariables(inputWindowInstance, modeComboBox, magPhaseRadio, innerRegion)
        self.addEventListeners()
    
    def setupVariables(self, inputWindowInstance, modeComboBox, magPhaseRadio, innerRegion):
        self.setFixedSize(300, 300)
        self.freqComponents = None
        self.magnitudeSpectrum = None
        self.magnitudeNormalized = None
        self.phaseSpectrum = None
        self.phaseNormalized = None
        self.realSpectrum = None
        self.realNormalized = None
        self.imaginarySpectrum = None
        self.imaginaryNormalized = None
        self.originalWindowInstance = inputWindowInstance
        self.modeComboBox = modeComboBox  # Combo box for choosing the spectrum that's shown in the UI container (magnitude or phase or real or imaginary)
        self.magPhaseRadio = magPhaseRadio  # Radio button that decides which of the fourier components are shown in the combobox (either magnitude & phase or real and imaginary)
        self.innerRegion = innerRegion # Radio button that decides which region the mixing should use (inner or outer)
        self.regionSelector = QRect(0, 0, self.width(), self.height())
        self.resizingRegion = False
        self.regionCorner = None # Which of the 4 corners of the region selector is the user clicking on
        
    def addEventListeners(self):
        self.originalWindowInstance.imageUpdatedSignal.connect(self.computeFreqComponents)  # When an input image is uploaded or updated, compute its fft
        self.modeComboBox.currentIndexChanged.connect(self.selectMode)
        self.magPhaseRadio.toggled.connect(self.selectMode)
        self.innerRegion.toggled.connect(self.onRegionToggled)
    
    def computeFreqComponents(self):
        if self.originalWindowInstance.image:
            logging.info("Started To Compute Fourier Components")
            originalQImage = self.originalWindowInstance.q_image
            width = self.originalWindowInstance.width
            height = self.originalWindowInstance.height 
            ptr = originalQImage.bits()
            ptr.setsize(width * height)
            originalImgArray = np.frombuffer(ptr, np.uint8).reshape((height, width)) # 2d array representing the img to compute its fourier transform

            self.freqComponents = np.fft.fft2(originalImgArray)
            shiftedFreqComponents = np.fft.fftshift(self.freqComponents) # Shifting frequencies to get the low frequencies in the middle
            
            self.magnitudeSpectrum = np.abs(shiftedFreqComponents)
            magnitudeLoggedSpectrum = np.log(self.magnitudeSpectrum) # taking the log to minimize its range
            self.magnitudeNormalized = cv2.normalize(magnitudeLoggedSpectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            self.phaseSpectrum = np.angle(shiftedFreqComponents)
            self.phaseNormalized = cv2.normalize(self.phaseSpectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            self.realSpectrum = np.real(shiftedFreqComponents)
            realLoggedSpectrum = np.log(self.realSpectrum)
            self.realNormalized = cv2.normalize(realLoggedSpectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
            
            self.imaginarySpectrum = np.imag(shiftedFreqComponents)
            self.imaginaryNormalized = cv2.normalize(self.imaginarySpectrum, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
            if self.magPhaseRadio.isChecked(): 
                self.showMagPhaseComponent()
            else:
                self.showRealImagComponent()

        else:
            logging.error("Tried To Compute Fourier For An Empty Input Image")

    def showMagPhaseComponent(self):
        if self.freqComponents is not None:
            if self.modeComboBox.currentIndex() == 0:
                height, width = self.magnitudeNormalized.shape
                freqQImage = QImage(self.magnitudeNormalized.data, width, height, width, QImage.Format_Grayscale8)
            else:
                height, width = self.phaseNormalized.shape
                freqQImage = QImage(self.phaseNormalized.data, width, height, width, QImage.Format_Grayscale8)

            freqSpectrumPixmap = QPixmap.fromImage(freqQImage)
            freqSpectrumScaledPixmap = freqSpectrumPixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation)
            self.setPixmap(freqSpectrumScaledPixmap)
            self.spectrumUpdatedSignal.emit()  
        
    def showRealImagComponent(self):
        if self.freqComponents is not None:
            if self.modeComboBox.currentIndex() == 0:
                height, width = self.realNormalized.shape
                freqQImage = QImage(self.realNormalized.data, width, height, width, QImage.Format_Grayscale8 )
            else:
                height, width = self.imaginaryNormalized.shape
                freqQImage = QImage(self.imaginaryNormalized.data, width, height, width, QImage.Format_Grayscale8 )
                
            freqSpectrumPixmap = QPixmap.fromImage(freqQImage)  
            freqSpectrumScaledPixmap = freqSpectrumPixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation)
            self.setPixmap(freqSpectrumScaledPixmap) 
            self.spectrumUpdatedSignal.emit()
     
    def selectMode(self):
        if self.magPhaseRadio.isChecked(): 
            self.modeComboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
            self.modeComboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
            self.showMagPhaseComponent()
                
        else:
            self.modeComboBox.setItemText(0, _translate("MainWindow", "FT Real"))
            self.modeComboBox.setItemText(1, _translate("MainWindow", "FT Img"))
            self.showRealImagComponent()
    
    def onRegionToggled(self):
        logging.info("Changed Region Type")
        self.update()  # Triggers the paintEvent method
        self.spectrumUpdatedSignal.emit()  

    # Check if the user clicked on any of the region's corners
    def mousePressEvent(self, event):
        if self.originalWindowInstance.image and self.regionSelector.contains(event.pos()):
            self.resizingRegion = True
            self.regionCorner = self.getCorner(event.pos())
    
    def getCorner(self, point):
        margin = 20  # Margin of error for detecting proximity to corners

        # Check proximity to each corner within the margin
        if abs(point.x() - self.regionSelector.left()) < margin and abs(point.y() - self.regionSelector.top()) < margin:
            return "topLeft"
        elif abs(point.x() - self.regionSelector.right()) < margin and abs(point.y() - self.regionSelector.top()) < margin:
            return "topRight"
        elif abs(point.x() - self.regionSelector.left()) < margin and abs(point.y() - self.regionSelector.bottom()) < margin:
            return "bottomLeft"
        elif abs(point.x() - self.regionSelector.right()) < margin and abs(point.y() - self.regionSelector.bottom()) < margin:
            return "bottomRight"
        else:
            logging.warning("Can't Resize Region Unless A Corner Is Pressed")
            return None

    def mouseMoveEvent(self, event):
        if self.resizingRegion and self.regionCorner:
            newRegion = self.regionSelector

            # Update the region size based on the corner being dragged
            if self.regionCorner == "topLeft":
                newRegion.setTopLeft(event.pos())
            elif self.regionCorner == "topRight":
                newRegion.setTopRight(event.pos())
            elif self.regionCorner == "bottomLeft":
                newRegion.setBottomLeft(event.pos())
            elif self.regionCorner == "bottomRight":
                newRegion.setBottomRight(event.pos())

            # Constrain the region within UI container boundaries
            newRegion.setLeft(max(0, newRegion.left()))
            newRegion.setTop(max(0, newRegion.top()))
            newRegion.setRight(min(self.width(), newRegion.right()))
            newRegion.setBottom(min(self.height(), newRegion.bottom()))

            # Ensure sides do not cross over
            if newRegion.left() >= newRegion.right():
                if self.regionCorner in ["topLeft", "bottomLeft"]:
                    newRegion.setLeft(newRegion.right() - 5)
                else:
                    newRegion.setRight(newRegion.left() + 5)

            if newRegion.top() >= newRegion.bottom():
                if self.regionCorner in ["topLeft", "topRight"]:
                    newRegion.setTop(newRegion.bottom() - 5)
                else:
                    newRegion.setBottom(newRegion.top() + 5)

            self.regionSelector = newRegion
            self.update()
            self.regionResizedSignal.emit()
            self.spectrumUpdatedSignal.emit()
        else:
            logging.error("Can't Resize An Invisible Region")

    def mouseReleaseEvent(self, event):
        self.resizingRegion = False
        self.regionCorner = None

    def paintEvent(self, event):
        super().paintEvent(event) # Combines the default QLabel rendering with our additions
        if not self.originalWindowInstance.image:
            return
        
        transparentRed = QColor(255, 0, 0, 20)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(transparentRed)

        # Draws the transparent colored part showcasing which region is selected (inside region selector or outside it)
        if self.innerRegion.isChecked():
            painter.drawRect(self.regionSelector)
        else:
            painter.drawRect(0, 0, self.width(), self.regionSelector.top())  # Top area
            painter.drawRect(0, self.regionSelector.bottom(), self.width(), self.height() - self.regionSelector.bottom())  # Bottom area
            painter.drawRect(0, self.regionSelector.top(), self.regionSelector.left(), self.regionSelector.height())  # Left area
            painter.drawRect(self.regionSelector.right(), self.regionSelector.top(), self.width() - self.regionSelector.right(), self.regionSelector.height())  # Right area

        # Draws handles at each corner of the region
        painter.setBrush(Qt.blue)
        cornerSize = 8
        painter.drawRect(self.regionSelector.topLeft().x() - cornerSize, self.regionSelector.topLeft().y() - cornerSize, cornerSize * 2, cornerSize * 2)
        painter.drawRect(self.regionSelector.topRight().x() - cornerSize, self.regionSelector.topRight().y() - cornerSize, cornerSize * 2, cornerSize * 2)
        painter.drawRect(self.regionSelector.bottomLeft().x() - cornerSize, self.regionSelector.bottomLeft().y() - cornerSize, cornerSize * 2, cornerSize * 2)
        painter.drawRect(self.regionSelector.bottomRight().x() - cornerSize, self.regionSelector.bottomRight().y() - cornerSize, cornerSize * 2, cornerSize * 2)
    
    # Needed for unifying all 4 different region selectors for component window class instances
    def getRegionVertices(self):
        return {
            "topLeft": self.regionSelector.topLeft(),
            "topRight": self.regionSelector.topRight(),
            "bottomLeft": self.regionSelector.bottomLeft(),
            "bottomRight": self.regionSelector.bottomRight(),
        }
    
    def setRegion(self, topLeft, topRight, bottomLeft, bottomRight):
        # Ensure the region is valid
        if topLeft.x() >= topRight.x() or bottomLeft.x() >= bottomRight.x() or topLeft.y() >= bottomLeft.y() or topRight.y() >= bottomRight.y():
            return

        # Set the rectangle based on the provided vertices
        self.regionSelector.setTopLeft(topLeft)
        self.regionSelector.setTopRight(topRight)
        self.regionSelector.setBottomLeft(bottomLeft)
        self.regionSelector.setBottomRight(bottomRight)

        # Constrain the rectangle within the UI cotnainer's bounds
        self.regionSelector.setLeft(max(0, self.regionSelector.left()))
        self.regionSelector.setTop(max(0, self.regionSelector.top()))
        self.regionSelector.setRight(min(self.width(), self.regionSelector.right()))
        self.regionSelector.setBottom(min(self.height(), self.regionSelector.bottom()))

        # Triggers the paintEvent method
        self.update()            
                     
class OutputWindow(QtWidgets.QLabel):
    def __init__(self, componentInstances, weights, magPhaseRadio, innerRegion, parent = None):
        super().__init__(parent)   
        self.setupVariables(componentInstances, weights, magPhaseRadio, innerRegion)
        self.addEventListeners()

    def setupVariables(self, componentInstances, weights, magPhaseRadio, innerRegion):
        self.setFixedSize(300, 300)
        self.componentInstances = componentInstances
        self.weights = weights
        self.magPhaseRadio = magPhaseRadio
        self.innerRegion = innerRegion
        self.outputScaledPixmap = None
        self.selected = False
    
    def addEventListeners(self):
        for componentInstance in self.componentInstances:
            componentInstance.spectrumUpdatedSignal.connect(self.showReconstructedImage)
        for weight in self.weights:
            weight.valueChanged.connect(self.showReconstructedImage)
            
    def showReconstructedImage(self):
        fullSpectrum = None
        for i in range(len(self.componentInstances)):
            if self.componentInstances[i].freqComponents is not None:
                fullSpectrum = self.componentInstances[i].magnitudeSpectrum
                break
        if fullSpectrum is None:
            logging.warning("Can't mix without an image being uploaded")
            return
        
        # y represent the rows, while x represent the columns
        xStart, yStart = self.componentInstances[0].regionSelector.left(), self.componentInstances[0].regionSelector.top()
        xEnd, yEnd = self.componentInstances[0].regionSelector.right(), self.componentInstances[0].regionSelector.bottom()

        if self.innerRegion.isChecked():
            croppedShape = fullSpectrum[yStart : yEnd, xStart : xEnd].shape
        else:
            croppedShape = fullSpectrum.shape
  
        self.totalMagnitudes = np.zeros(croppedShape)
        self.totalPhases = np.zeros(croppedShape)
        self.totalReal = np.zeros(croppedShape)
        self.totalImaginary = np.zeros(croppedShape)

        for i in range(len(self.componentInstances)):
            if self.componentInstances[i].freqComponents is not None:
                if self.innerRegion.isChecked():
                    currMagnitude = self.componentInstances[i].magnitudeSpectrum[yStart : yEnd, xStart : xEnd]
                    currPhase = self.componentInstances[i].phaseSpectrum[yStart : yEnd, xStart : xEnd]
                    currReal = self.componentInstances[i].realSpectrum[yStart : yEnd, xStart : xEnd]
                    currImaginary = self.componentInstances[i].imaginarySpectrum[yStart : yEnd, xStart : xEnd]
                    
                else:
                    # Outer regions (top, bottom, left, and right)
                    currMagnitude = np.zeros_like(fullSpectrum)
                    currPhase = np.zeros_like(fullSpectrum)
                    currReal = np.zeros_like(fullSpectrum)
                    currImaginary = np.zeros_like(fullSpectrum)

                    self.fillOuterRegions(currMagnitude, self.componentInstances[i].magnitudeSpectrum, yStart, yEnd, xStart, xEnd)
                    self.fillOuterRegions(currPhase, self.componentInstances[i].phaseSpectrum, yStart, yEnd, xStart, xEnd)
                    self.fillOuterRegions(currReal, self.componentInstances[i].realSpectrum, yStart, yEnd, xStart, xEnd)
                    self.fillOuterRegions(currImaginary, self.componentInstances[i].imaginarySpectrum, yStart, yEnd, xStart, xEnd)

                self.totalMagnitudes += self.weights[i].value() / 100.0 * currMagnitude
                self.totalPhases += self.weights[i].value() / 100.0 * currPhase
                self.totalReal += self.weights[i].value() / 100.0 * currReal
                self.totalImaginary += self.weights[i].value() / 100.0 * currImaginary
            
        if self.magPhaseRadio.isChecked(): 
            reconstructedFreqComponents = self.totalMagnitudes * np.exp(1j * self.totalPhases)
        else: 
            reconstructedFreqComponents = self.totalReal + 1j * self.totalImaginary
            
        reconstructedImgArray = np.abs(np.fft.ifft2(reconstructedFreqComponents))
        reconstructedImgNormalizedArray = cv2.normalize(reconstructedImgArray, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        height, width = reconstructedImgNormalizedArray.shape
        reconstructedQImage = QImage(reconstructedImgNormalizedArray.data, width, height, width, QImage.Format_Grayscale8 )
        outputPixmap = QPixmap.fromImage(reconstructedQImage)
        self.outputScaledPixmap = outputPixmap.scaled(self.size(), transformMode= Qt.SmoothTransformation)
        if self.selected:
            self.setPixmap(self.outputScaledPixmap)
    
    # Gets the fourier components of the outer region
    def fillOuterRegions(self, currSpectrum, sourceSpectrum, yStart, yEnd, xStart, xEnd):
        # Top region
        currSpectrum[:yStart, :] = sourceSpectrum[:yStart, :]
        # Bottom region
        currSpectrum[yEnd:, :] = sourceSpectrum[yEnd:, :]
        # Left region
        currSpectrum[yStart:yEnd, :xStart] = sourceSpectrum[yStart:yEnd, :xStart]
        # Right region
        currSpectrum[yStart:yEnd, xEnd:] = sourceSpectrum[yStart:yEnd, xEnd:]