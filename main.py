from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Load the UI file
        self.setupUi(self)
        self.setupVariables()
        self.addEventListeners()
        self.selectOutputPort()
        self.show()
        
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
            container.regionResizedSignal.connect(self.unifyRegionSelectors)
        
        self.radioButton1.toggled.connect(self.selectOutputPort)
    
    def unifyRegionSelectors(self):
        triggeringContainer = self.sender() # gets the currently changed rectangle so that the other rectangles are shaped according to it
        vertices = triggeringContainer.getRegionVertices()
        topLeft = vertices["topLeft"]
        topRight = vertices["topRight"]
        bottomLeft = vertices["bottomLeft"]
        bottomRight = vertices["bottomRight"]

        for container in self.fourierContainers:
            container.setRegion(topLeft, topRight, bottomLeft, bottomRight)
    
    def selectOutputPort(self):
        if self.radioButton1.isChecked():
            self.output2_port.clear()
            self.output2_port.selected = False

            self.output1_port.selected = True
            if self.output1_port.outputScaledPixmap is not None:
                self.output1_port.setPixmap(self.output1_port.outputScaledPixmap)            
        else:
            self.output1_port.clear()
            self.output1_port.selected = False

            self.output2_port.selected = True
            if self.output2_port.outputScaledPixmap is not None:
                self.output2_port.setPixmap(self.output2_port.outputScaledPixmap)
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
