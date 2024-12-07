
from PyQt5 import QtCore, QtGui, QtWidgets
from classes import InputWindow, OutputWindow, ComponentWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 749)
        MainWindow.setStyleSheet("<property name=\"styleSheet\">\n"
"   <string notr=\"true\">\n"
"    /* Modern Dark Theme */\n"
"    QMainWindow {\n"
"        background-color: #1e1e2e;\n"
"    }\n"
"    \n"
"    QPushButton {\n"
"        background-color: #7c3aed;\n"
"        border-radius: 8px;\n"
"        color: white;\n"
"        padding: 8px 16px;\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"        border: none;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #6d28d9;\n"
"    }\n"
"    \n"
"    QPushButton:pressed {\n"
"        background-color: #5b21b6;\n"
"    }\n"
"    \n"
"    QComboBox {\n"
"        padding: 6px;\n"
"        border: 2px solid #7c3aed;\n"
"        border-radius: 6px;\n"
"        background: rgba(124, 58, 237, 0.1);\n"
"        color: white;\n"
"        font-size: 12px;\n"
"    }\n"
"    \n"
"    QRadioButton {\n"
"        color: white;\n"
"        spacing: 8px;\n"
"        font-weight: bold;\n"
"        font-size: 13px;\n"
"    }\n"
"    \n"
"    QRadioButton::indicator {\n"
"        width: 16px;\n"
"        height: 16px;\n"
"        border-radius: 8px;\n"
"        border: 2px solid #7c3aed;\n"
"    }\n"
"    \n"
"    QRadioButton::indicator:checked {\n"
"        background-color: #7c3aed;\n"
"    }\n"
"    \n"
"    QProgressBar {\n"
"        border: 2px solid #7c3aed;\n"
"        border-radius: 5px;\n"
"        text-align: center;\n"
"        color: white;\n"
"        background-color: #2a2a3c;\n"
"    }\n"
"    \n"
"    QProgressBar::chunk {\n"
"        background-color: #7c3aed;\n"
"        border-radius: 3px;\n"
"    }\n"
"    \n"
"    QFrame {\n"
"        background-color: #2a2a3c;\n"
"        border-radius: 12px;\n"
"        border: 1px solid #3f3f5c;\n"
"        padding: 10px;\n"
"    }\n"
"\n"
"    QLabel {\n"
"        color: white;\n"
"        font-size: 13px;\n"
"    }\n"
"\n"
"    Line {\n"
"        background-color: #3f3f5c;\n"
"        border-radius: 5px;\n"
"    }\n"
"   </string>\n"
"</property>")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #1b1d23;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_left = QtWidgets.QVBoxLayout()
        self.verticalLayout_left.setObjectName("verticalLayout_left")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(39, 44, 54);\n"
"border: none;\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_3.addWidget(self.line_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;\n"
"font-weight:10000px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.original1 = InputWindow(self.frame)
        self.original1.setStyleSheet("QWidget {\n"
" border: 3px solid rgb(17,17,17);\n"
"}")
        self.original1.setObjectName("original1")
        self.verticalLayout.addWidget(self.original1)
        self.verticalLayout.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.component_image1 = ComponentWindow(self.frame)
        self.component_image1.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.component_image1.setObjectName("component_image1")
        self.verticalLayout_2.addWidget(self.component_image1)
        self.verticalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Slider_weight1 = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_weight1.sizePolicy().hasHeightForWidth())
        self.Slider_weight1.setSizePolicy(sizePolicy)
        self.Slider_weight1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_weight1.setObjectName("Slider_weight1")
        self.horizontalLayout.addWidget(self.Slider_weight1)
        self.combo1 = QtWidgets.QComboBox(self.frame)
        self.combo1.setStyleSheet("QComboBox {\n"
"    font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */\n"
"    border: 1px solid white; /* Set the border to 1px solid white */\n"
"background: rgba(74, 74, 74, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.horizontalLayout.addWidget(self.combo1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_left.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_12 = QtWidgets.QFrame(self.frame_2)
        self.line_12.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_4.addWidget(self.line_12)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.original2 = InputWindow(self.frame_2)
        self.original2.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.original2.setObjectName("original2")
        self.verticalLayout_5.addWidget(self.original2)
        self.verticalLayout_5.setStretch(1, 5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.component_image2 = ComponentWindow(self.frame_2)
        self.component_image2.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.component_image2.setObjectName("component_image2")
        self.verticalLayout_6.addWidget(self.component_image2)
        self.verticalLayout_6.setStretch(1, 5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Slider_weight2 = QtWidgets.QSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_weight2.sizePolicy().hasHeightForWidth())
        self.Slider_weight2.setSizePolicy(sizePolicy)
        self.Slider_weight2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_weight2.setObjectName("Slider_weight2")
        self.horizontalLayout_3.addWidget(self.Slider_weight2)
        self.combo2 = QtWidgets.QComboBox(self.frame_2)
        self.combo2.setStyleSheet("QComboBox {\n"
"    font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */\n"
"    border: 1px solid white; /* Set the border to 1px solid white */\n"
"background: rgba(74, 74, 74, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("")
        self.combo2.addItem("")
        self.horizontalLayout_3.addWidget(self.combo2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_left.addWidget(self.frame_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_left)
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        self.verticalLayout_right.setObjectName("verticalLayout_right")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.line_11 = QtWidgets.QFrame(self.frame_3)
        self.line_11.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_9.addWidget(self.line_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.original3 = InputWindow(self.frame_3)
        self.original3.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.original3.setObjectName("original3")
        self.verticalLayout_10.addWidget(self.original3)
        self.verticalLayout_10.setStretch(1, 5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        self.component_image3 =ComponentWindow(self.frame_3)
        self.component_image3.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.component_image3.setObjectName("component_image3")
        self.verticalLayout_11.addWidget(self.component_image3)
        self.verticalLayout_11.setStretch(1, 5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Slider_weight3 = QtWidgets.QSlider(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_weight3.sizePolicy().hasHeightForWidth())
        self.Slider_weight3.setSizePolicy(sizePolicy)
        self.Slider_weight3.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_weight3.setObjectName("Slider_weight3")
        self.horizontalLayout_5.addWidget(self.Slider_weight3)
        self.combo3 = QtWidgets.QComboBox(self.frame_3)
        self.combo3.setStyleSheet("QComboBox {\n"
"    font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */\n"
"    border: 1px solid white; /* Set the border to 1px solid white */\n"
"background: rgba(74, 74, 74, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.combo3.setObjectName("combo3")
        self.combo3.addItem("")
        self.combo3.addItem("")
        self.horizontalLayout_5.addWidget(self.combo3)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_right.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.line_14 = QtWidgets.QFrame(self.frame_4)
        self.line_14.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_12.addWidget(self.line_14)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter)
        self.original4 = InputWindow(self.frame_4)
        self.original4.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.original4.setObjectName("original4")
        self.verticalLayout_13.addWidget(self.original4)
        self.verticalLayout_13.setStretch(1, 5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.component_image4 = ComponentWindow(self.frame_4)
        self.component_image4.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.component_image4.setObjectName("component_image4")
        self.verticalLayout_14.addWidget(self.component_image4)
        self.verticalLayout_14.setStretch(1, 5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Slider_weight4 = QtWidgets.QSlider(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_weight4.sizePolicy().hasHeightForWidth())
        self.Slider_weight4.setSizePolicy(sizePolicy)
        self.Slider_weight4.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_weight4.setObjectName("Slider_weight4")
        self.horizontalLayout_7.addWidget(self.Slider_weight4)
        self.combo4 = QtWidgets.QComboBox(self.frame_4)
        self.combo4.setStyleSheet("QComboBox {\n"
"    font-family: \"Overpass\";\n"
"    font-weight: 600; /* Semibold */\n"
"    font-size: 10pt; /* Adjust the font size as needed */\n"
"    color: white; /* Set the text color to white */\n"
"    border: 1px solid white; /* Set the border to 1px solid white */\n"
"background: rgba(74, 74, 74, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.combo4.setObjectName("combo4")
        self.combo4.addItem("")
        self.combo4.addItem("")
        self.horizontalLayout_7.addWidget(self.combo4)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.verticalLayout_right.addWidget(self.frame_4)
        self.horizontalLayout_11.addLayout(self.verticalLayout_right)
        self.frame_right = QtWidgets.QFrame(self.centralwidget)
        self.frame_right.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 10px;\n"
"border: none;")
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_right)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.mixerOutputTo = QtWidgets.QLabel(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Overpass Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.mixerOutputTo.setFont(font)
        self.mixerOutputTo.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.mixerOutputTo.setObjectName("mixerOutputTo")
        self.verticalLayout_18.addWidget(self.mixerOutputTo, 0, QtCore.Qt.AlignHCenter)
        self.line_15 = QtWidgets.QFrame(self.frame_right)
        self.line_15.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_18.addWidget(self.line_15)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_Routput = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Routput.setObjectName("horizontalLayout_Routput")
        self.radioButton1 = QtWidgets.QRadioButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton1.setFont(font)
        self.radioButton1.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.radioButton1.setObjectName("radioButton1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton1)
        self.horizontalLayout_Routput.addWidget(self.radioButton1, 0, QtCore.Qt.AlignHCenter)
        self.radioButton2 = QtWidgets.QRadioButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton2.setFont(font)
        self.radioButton2.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.radioButton2.setObjectName("radioButton2")
        self.buttonGroup.addButton(self.radioButton2)
        self.horizontalLayout_Routput.addWidget(self.radioButton2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_17.addLayout(self.horizontalLayout_Routput)
        self.horizontalLayout_output = QtWidgets.QHBoxLayout()
        self.horizontalLayout_output.setContentsMargins(-1, -1, -1, 11)
        self.horizontalLayout_output.setObjectName("horizontalLayout_output")
        self.verticalLayout_OP1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_OP1.setObjectName("verticalLayout_OP1")
        self.label_op1 = QtWidgets.QLabel(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_op1.setFont(font)
        self.label_op1.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_op1.setObjectName("label_op1")
        self.verticalLayout_OP1.addWidget(self.label_op1, 0, QtCore.Qt.AlignHCenter)
        self.output1_port = OutputWindow(self.frame_right)
        self.output1_port.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.output1_port.setObjectName("output1_port")
        self.verticalLayout_OP1.addWidget(self.output1_port)
        self.verticalLayout_OP1.setStretch(1, 5)
        self.horizontalLayout_output.addLayout(self.verticalLayout_OP1)
        self.verticalLayout_OP2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_OP2.setObjectName("verticalLayout_OP2")
        self.label_op2 = QtWidgets.QLabel(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_op2.setFont(font)
        self.label_op2.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.label_op2.setObjectName("label_op2")
        self.verticalLayout_OP2.addWidget(self.label_op2, 0, QtCore.Qt.AlignHCenter)
        self.output2_port = OutputWindow(self.frame_right)
        self.output2_port.setStyleSheet("border: 3px solid rgb(17,17,17);")
        self.output2_port.setObjectName("output2_port")
        self.verticalLayout_OP2.addWidget(self.output2_port)
        self.verticalLayout_OP2.setStretch(1, 5)
        self.horizontalLayout_output.addLayout(self.verticalLayout_OP2)
        self.verticalLayout_17.addLayout(self.horizontalLayout_output)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.mixxer = QtWidgets.QPushButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("-apple-system")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mixxer.setFont(font)
        self.mixxer.setStyleSheet("QPushButton{\n"
"  appearance: button;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  height: 30px;\n"
"  margin: 0 20px 0 20px;\n"
"  position: center;\n"
"  width:70px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #283999;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #1c2973;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/combine-svgrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mixxer.setIcon(icon)
        self.mixxer.setIconSize(QtCore.QSize(25, 25))
        self.mixxer.setObjectName("mixxer")
        self.horizontalLayout_10.addWidget(self.mixxer)
        self.progressBar = QtWidgets.QProgressBar(self.frame_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_10.addWidget(self.progressBar)
        self.verticalLayout_18.addLayout(self.horizontalLayout_10)
        self.line_17 = QtWidgets.QFrame(self.frame_right)
        self.line_17.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_18.addWidget(self.line_17)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.selectedArea = QtWidgets.QLabel(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Overpass Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.selectedArea.setFont(font)
        self.selectedArea.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.selectedArea.setObjectName("selectedArea")
        self.verticalLayout_15.addWidget(self.selectedArea, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.radioButton_In = QtWidgets.QRadioButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_In.setFont(font)
        self.radioButton_In.setStyleSheet("color:white;\n"
"font-weight:10000px;\n"
"")
        self.radioButton_In.setObjectName("radioButton_In")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_In)
        self.verticalLayout_7.addWidget(self.radioButton_In, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_Out = QtWidgets.QRadioButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_Out.setFont(font)
        self.radioButton_Out.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.radioButton_Out.setObjectName("radioButton_Out")
        self.buttonGroup_2.addButton(self.radioButton_Out)
        self.verticalLayout_7.addWidget(self.radioButton_Out, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.Deselect = QtWidgets.QPushButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("-apple-system")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Deselect.setFont(font)
        self.Deselect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Deselect.setStyleSheet("QPushButton{\n"
"  appearance: button;\n"
"  background-color: #405cf5;\n"
"  border-radius: 6px;\n"
"  border-width: 0;\n"
"  box-shadow: rgba(50, 50, 93, .1) 0 0 0 1px inset,rgba(50, 50, 93, .1) 0 2px 5px 0,rgba(0, 0, 0, .07) 0 1px 1px 0;\n"
"  color: #fff;\n"
"  cursor: pointer;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Roboto,\"Helvetica Neue\",Ubuntu,sans-serif;\n"
"  height: 30px;\n"
"  margin: 0 20px 0 20px;\n"
"  position: center;\n"
"  width:70px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #283999;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #1c2973;\n"
"}\n"
"")
        self.Deselect.setIconSize(QtCore.QSize(25, 20))
        self.Deselect.setObjectName("Deselect")
        self.horizontalLayout_9.addWidget(self.Deselect)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.verticalLayout_16.addLayout(self.verticalLayout_15)
        self.verticalLayout_18.addLayout(self.verticalLayout_16)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.line_18 = QtWidgets.QFrame(self.frame_right)
        self.line_18.setStyleSheet("/* Line style */\n"
"\n"
"  /* Set the width of the line */\n"
"  width: 20px;\n"
"\n"
"  /* Set the height of the line */\n"
"  height: 5px;\n"
"\n"
"  /* Set the background color of the line */\n"
"  background-color:rgb(77, 86, 105);\n"
"\n"
"  /* Set the border of the line */\n"
"  border: 10px;\n"
"\n"
"  /* Set the border radius of the line */\n"
"  border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_19.addWidget(self.line_18)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.selectedArea_2 = QtWidgets.QLabel(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Overpass Black")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.selectedArea_2.setFont(font)
        self.selectedArea_2.setStyleSheet("color:white;\n"
"font-size:20px;\n"
"margin: 0 0 ;")
        self.selectedArea_2.setObjectName("selectedArea_2")
        self.verticalLayout_20.addWidget(self.selectedArea_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.mode1 = QtWidgets.QRadioButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mode1.setFont(font)
        self.mode1.setStyleSheet("color:white;\n"
"font-weight:10000px;\n"
"")
        self.mode1.setObjectName("mode1")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.mode1)
        self.verticalLayout_21.addWidget(self.mode1, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_21.addItem(spacerItem)
        self.mode2 = QtWidgets.QRadioButton(self.frame_right)
        font = QtGui.QFont()
        font.setFamily("Oswald SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mode2.setFont(font)
        self.mode2.setStyleSheet("color:white;\n"
"font-weight:10000px;")
        self.mode2.setObjectName("mode2")
        self.buttonGroup_3.addButton(self.mode2)
        self.verticalLayout_21.addWidget(self.mode2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_14.addLayout(self.verticalLayout_21)
        self.verticalLayout_20.addLayout(self.horizontalLayout_14)
        self.verticalLayout_19.addLayout(self.verticalLayout_20)
        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        spacerItem1 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_18.addItem(spacerItem1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_18.addLayout(self.verticalLayout_8)
        self.verticalLayout_18.setStretch(2, 2)
        self.horizontalLayout_11.addWidget(self.frame_right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1293, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Original Image"))
        self.label_3.setText(_translate("MainWindow", "FT Component"))
        self.combo1.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.combo1.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.label_5.setText(_translate("MainWindow", "Original Image"))
        self.label_6.setText(_translate("MainWindow", "FT Component"))
        self.combo2.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.combo2.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.label_8.setText(_translate("MainWindow", "Original Image"))
        self.label_9.setText(_translate("MainWindow", "FT Component"))
        self.combo3.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.combo3.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.label_11.setText(_translate("MainWindow", "Original Image"))
        self.label_12.setText(_translate("MainWindow", "FT Component"))
        self.combo4.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.combo4.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.mixerOutputTo.setText(_translate("MainWindow", "Mixer Output To:"))
        self.radioButton1.setText(_translate("MainWindow", "Output 1"))
        self.radioButton2.setText(_translate("MainWindow", "Output 2"))
        self.label_op1.setText(_translate("MainWindow", "Output 1"))
        self.label_op2.setText(_translate("MainWindow", "Output 2"))
        self.mixxer.setText(_translate("MainWindow", "Mix"))
        self.selectedArea.setText(_translate("MainWindow", "Selected Area"))
        self.radioButton_In.setText(_translate("MainWindow", "Inside Region"))
        self.radioButton_Out.setText(_translate("MainWindow", "Outside Region"))
        self.Deselect.setText(_translate("MainWindow", "Deselect"))
        self.selectedArea_2.setText(_translate("MainWindow", "Select Mode"))
        self.mode1.setText(_translate("MainWindow", "Mag and Phase"))
        self.mode2.setText(_translate("MainWindow", "Real and Imaginary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
