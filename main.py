from PyQt5 import QtWidgets, uic
from MainWindow import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Load the UI file
        self.setupUi(self)
        #uic.loadUi('MainWindow.ui', self)
        self.setupVariables()
        self.addEventListeners()
        self.show()
    
    def setupVariables(self):
        self.minWidth = 300
        self.minHeight = 300
        self.imageContainers = [self.original1, self.original2, self.original3, self.original4]
    
    def addEventListeners(self):
        # for img in self.imageContainers:
        #     img.isBrowsed.connect(self.uniformSize)
        pass

    # def uniformSize(self):
    #     for img in self.imageContainers:
    #         if img.width != 0:
    #             if (self.minWidth == 0 or (img.width * img.height < self.minWidth * self.minHeight)):
    #                 self.minWidth = img.width
    #                 self.minHeight = img.height
                    

    #     if self.minWidth != 0:    
    #         for img in self.imageContainers:
    #             if img.width != 0 and img.uploaded:
    #                 img.width = self.minWidth 
    #                 img.height = self.minHeight 
    #                 img.addImage()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()