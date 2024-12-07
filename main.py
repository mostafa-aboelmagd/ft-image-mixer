# i want to visualize the MainWindow applicatrion using PyQt5

from PyQt5 import QtWidgets, uic
from MainWindow import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Load the UI file
        self.setupUi(self)
        #uic.loadUi('MainWindow.ui', self)
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()