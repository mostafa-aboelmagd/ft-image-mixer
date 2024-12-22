from PyQt5 import QtWidgets, uic, QtCore
from MainWindow import Ui_MainWindow
import sys

# _translate = QtCore.QCoreApplication.translate
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Load the UI file
        self.setupUi(self)
        #uic.loadUi('MainWindow.ui', self)
        self.setupVariables()
        self.addEventListeners()
        # self.selectMode()
        self.show()
        self.selectOutputPort() # selecting the initial output port that is checked when the application starts
        
    def setupVariables(self):
        self.imageContainers = [self.original1, self.original2, self.original3, self.original4]
        self.fourierContainers = [self.component_image1, self.component_image2, self.component_image3, self.component_image4]
        self.sliders = [self.Slider_weight1, self.Slider_weight2, self.Slider_weight3, self.Slider_weight4]
        for slider in self.sliders:
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(100)
            slider.setTickInterval(10)
            
    def addEventListeners(self):
        for container in self.fourierContainers:
            container.regionChanged.connect(self.unifyRegionSelectors)
        
        self.radioButton1.toggled.connect(self.selectOutputPort) # selecting the output port when toggling ports
        self.mode1.toggled.connect(self.selectOutputPort)  # to keep the selected output port when toggling modes
        self.mode2.toggled.connect(self.selectOutputPort)
        self.combo1.currentIndexChanged.connect(self.selectOutputPort) # to keep the selected output port when changing comboBox selection
        self.combo2.currentIndexChanged.connect(self.selectOutputPort)
        self.combo3.currentIndexChanged.connect(self.selectOutputPort)
        self.combo4.currentIndexChanged.connect(self.selectOutputPort)
        self.original1.imageUpdatedSignal.connect(self.selectOutputPort) # to keep the selected output port when updating the input image
        self.original2.imageUpdatedSignal.connect(self.selectOutputPort)
        self.original3.imageUpdatedSignal.connect(self.selectOutputPort)
        self.original4.imageUpdatedSignal.connect(self.selectOutputPort)
    
    def unifyRegionSelectors(self):
        triggeringContainer = self.sender() # gets the currently changed rectangle so that the other rectangles are shaped according to it
        vertices = triggeringContainer.getRectangleVertices()
        top_left = vertices["topLeft"]
        top_right = vertices["topRight"]
        bottom_left = vertices["bottomLeft"]
        bottom_right = vertices["bottomRight"]

        for container in self.fourierContainers:
            container.setRectangle(top_left, top_right, bottom_left, bottom_right)
    
    def selectOutputPort(self):
        if self.radioButton1.isChecked():
            if self.output1_port.output_scaled_pixmap is not None:
                self.output1_port.setPixmap(self.output1_port.output_scaled_pixmap)
            self.output2_port.clear()
            
        else:
            self.output1_port.clear()
            if self.output2_port.output_scaled_pixmap is not None:
                self.output2_port.setPixmap(self.output2_port.output_scaled_pixmap)
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    