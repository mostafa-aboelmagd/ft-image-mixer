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
        self.imageContainers = [self.original1, self.original2, self.original3, self.original4]
    
    def addEventListeners(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()