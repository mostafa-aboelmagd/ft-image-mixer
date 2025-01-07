
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1650, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1650, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(1650, 1100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("/* General QWidget Style */\n"
"QWidget {\n"
"    background-color: #2E3440;\n"
"    color: #D8DEE9;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"/* PushButtons */\n"
"QPushButton {\n"
"    background-color: #4C566A;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #81A1C1;\n"
"    border-radius: 5px;\n"
"    padding: 5px 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #81A1C1;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #5E81AC;\n"
"}\n"
"\n"
"/* SpinBoxes */\n"
"QSpinBox {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #81A1C1;\n"
"    border-radius: 3px;\n"
"    padding: 2px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 12px;\n"
"    border-left: 1px solid #81A1C1;\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 12px;\n"
"    border-left: 1px solid #81A1C1;\n"
"}\n"
"\n"
"/* Horizontal Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #81A1C1;\n"
"    height: 5px;\n"
"    background: #3B4252;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #81A1C1;\n"
"    border: 1px solid #5E81AC;\n"
"    width: 15px;\n"
"    margin: -5px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #ECEFF4;\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* CheckBoxes */\n"
"QCheckBox {\n"
"    color: #ECEFF4;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #81A1C1;\n"
"    background-color: #2E3440;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #81A1C1;\n"
"    border: 1px solid #5E81AC;\n"
"}\n"
"\n"
"/* ComboBoxes */\n"
"QComboBox {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #81A1C1;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3B4252;\n"
"    color: #ECEFF4;\n"
"    border: 1px solid #81A1C1;\n"
"}\n"
"\n"
"/* LCD Number */\n"
"QLCDNumber {\n"
"    background-color: #3B4252;\n"
"    color: #81A1C1;\n"
"    border: 2px solid #81A1C1;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* QPolarChart */\n"
"QPolarChart {\n"
"    background: transparent;\n"
"}\n"
"QPolarChart > .chart-title {\n"
"    color: #ECEFF4;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"}\n"
"QPolarChart > .axis-title {\n"
"    color: #D8DEE9;\n"
"}\n"
"\n"
"/* Scrollbars */\n"
"QScrollBar:horizontal, QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2E3440;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal, QScrollBar::handle:vertical {\n"
"    background: #4C566A;\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(600, 150))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 400, 401, 511))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.beamControlDock = QtWidgets.QDockWidget(parent=self.verticalLayoutWidget_3)
        self.beamControlDock.setMaximumSize(QtCore.QSize(524287, 500))
        self.beamControlDock.setFloating(False)
        self.beamControlDock.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.beamControlDock.setObjectName("beamControlDock")
        self.beamControlContents = QtWidgets.QWidget()
        self.beamControlContents.setObjectName("beamControlContents")
        self.beamControlLayout_3 = QtWidgets.QVBoxLayout(self.beamControlContents)
        self.beamControlLayout_3.setObjectName("beamControlLayout_3")
        self.beamControlGroup = QtWidgets.QGroupBox(parent=self.beamControlContents)
        self.beamControlGroup.setObjectName("beamControlGroup")
        self.beamLayout_3 = QtWidgets.QVBoxLayout(self.beamControlGroup)
        self.beamLayout_3.setObjectName("beamLayout_3")
        self.steeringLayout = QtWidgets.QFormLayout()
        self.steeringLayout.setObjectName("steeringLayout")
        self.labelSteering = QtWidgets.QLabel(parent=self.beamControlGroup)
        self.labelSteering.setObjectName("labelSteering")
        self.steeringLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelSteering)
        self.steeringAngleLayout = QtWidgets.QHBoxLayout()
        self.steeringAngleLayout.setSpacing(0)
        self.steeringAngleLayout.setObjectName("steeringAngleLayout")
        self.steeringAngle = QtWidgets.QSlider(parent=self.beamControlGroup)
        self.steeringAngle.setMinimum(-90)
        self.steeringAngle.setMaximum(90)
        self.steeringAngle.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.steeringAngle.setObjectName("steeringAngle")
        self.steeringAngleLayout.addWidget(self.steeringAngle)
        self.steeringValue = QtWidgets.QLabel(parent=self.beamControlGroup)
        self.steeringValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.steeringValue.setIndent(0)
        self.steeringValue.setObjectName("steeringValue")
        self.steeringAngleLayout.addWidget(self.steeringValue)
        self.label_2 = QtWidgets.QLabel(parent=self.beamControlGroup)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.steeringAngleLayout.addWidget(self.label_2)
        self.steeringLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.steeringAngleLayout)
        self.beamLayout_3.addLayout(self.steeringLayout)
        self.comboBox = QtWidgets.QComboBox(parent=self.beamControlGroup)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.beamLayout_3.addWidget(self.comboBox)
        self.frequencyListGroup = QtWidgets.QGroupBox(parent=self.beamControlGroup)
        self.frequencyListGroup.setObjectName("frequencyListGroup")
        self.frequencyListLayout_3 = QtWidgets.QVBoxLayout(self.frequencyListGroup)
        self.frequencyListLayout_3.setObjectName("frequencyListLayout_3")
        self.frequencyList = QtWidgets.QListWidget(parent=self.frequencyListGroup)
        self.frequencyList.setObjectName("frequencyList")
        self.frequencyListLayout_3.addWidget(self.frequencyList)
        self.frequencyControlLayout = QtWidgets.QHBoxLayout()
        self.frequencyControlLayout.setObjectName("frequencyControlLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.frequencyListGroup)
        self.label_3.setObjectName("label_3")
        self.frequencyControlLayout.addWidget(self.label_3)
        self.frequencyInput = QtWidgets.QSpinBox(parent=self.frequencyListGroup)
        self.frequencyInput.setMinimumSize(QtCore.QSize(0, 0))
        self.frequencyInput.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frequencyInput.setMinimum(1)
        self.frequencyInput.setMaximum(1000000000)
        self.frequencyInput.setProperty("value", 1000)
        self.frequencyInput.setObjectName("frequencyInput")
        self.frequencyControlLayout.addWidget(self.frequencyInput)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.frequencyListGroup)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.frequencyControlLayout.addWidget(self.comboBox_2)
        self.frequencyListLayout_3.addLayout(self.frequencyControlLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frequencyListGroup)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.amplitudeInput = QtWidgets.QSpinBox(parent=self.frequencyListGroup)
        self.amplitudeInput.setMinimumSize(QtCore.QSize(0, 0))
        self.amplitudeInput.setMaximumSize(QtCore.QSize(30, 16777215))
        self.amplitudeInput.setSingleStep(1)
        self.amplitudeInput.setStepType(QtWidgets.QAbstractSpinBox.StepType.DefaultStepType)
        self.amplitudeInput.setProperty("value", 1)
        self.amplitudeInput.setObjectName("amplitudeInput")
        self.horizontalLayout_3.addWidget(self.amplitudeInput)
        self.label_5 = QtWidgets.QLabel(parent=self.frequencyListGroup)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.phaseInput = QtWidgets.QSpinBox(parent=self.frequencyListGroup)
        self.phaseInput.setMinimum(-180)
        self.phaseInput.setMaximum(180)
        self.phaseInput.setObjectName("phaseInput")
        self.horizontalLayout_3.addWidget(self.phaseInput)
        self.frequencyListLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addFrequencyButton = QtWidgets.QPushButton(parent=self.frequencyListGroup)
        self.addFrequencyButton.setObjectName("addFrequencyButton")
        self.horizontalLayout_4.addWidget(self.addFrequencyButton)
        self.removeFrequencyButton = QtWidgets.QPushButton(parent=self.frequencyListGroup)
        self.removeFrequencyButton.setObjectName("removeFrequencyButton")
        self.horizontalLayout_4.addWidget(self.removeFrequencyButton)
        self.frequencyListLayout_3.addLayout(self.horizontalLayout_4)
        self.beamLayout_3.addWidget(self.frequencyListGroup)
        self.widget_2 = QtWidgets.QWidget(parent=self.beamControlGroup)
        self.widget_2.setObjectName("widget_2")
        self.beamLayout_3.addWidget(self.widget_2)
        self.beamControlLayout_3.addWidget(self.beamControlGroup)
        self.beamControlDock.setWidget(self.beamControlContents)
        self.verticalLayout_21.addWidget(self.beamControlDock)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(410, 400, 1101, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BeamProfile = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.BeamProfile.setEnabled(True)
        self.BeamProfile.setMaximumSize(QtCore.QSize(1000, 483))
        self.BeamProfile.setObjectName("BeamProfile")
        self.horizontalLayout.addWidget(self.BeamProfile)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1374, 378))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_3 = QtWidgets.QWidget(parent=self.verticalLayoutWidget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4.addWidget(self.widget_3)
        self.arrayManagerDock = QtWidgets.QDockWidget(parent=self.verticalLayoutWidget_2)
        self.arrayManagerDock.setMaximumSize(QtCore.QSize(524287, 550))
        self.arrayManagerDock.setObjectName("arrayManagerDock")
        self.arrayManagerContents_4 = QtWidgets.QWidget()
        self.arrayManagerContents_4.setObjectName("arrayManagerContents_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.arrayManagerContents_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.positionGroup_2 = QtWidgets.QGroupBox(parent=self.arrayManagerContents_4)
        self.positionGroup_2.setObjectName("positionGroup_2")
        self.formLayout_12 = QtWidgets.QFormLayout(self.positionGroup_2)
        self.formLayout_12.setObjectName("formLayout_12")
        self.labelX_2 = QtWidgets.QLabel(parent=self.positionGroup_2)
        self.labelX_2.setObjectName("labelX_2")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelX_2)
        self.xPosition_target = QtWidgets.QDoubleSpinBox(parent=self.positionGroup_2)
        self.xPosition_target.setMinimum(-100.0)
        self.xPosition_target.setMaximum(100.0)
        self.xPosition_target.setSingleStep(0.1)
        self.xPosition_target.setObjectName("xPosition_target")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.xPosition_target)
        self.labelY_2 = QtWidgets.QLabel(parent=self.positionGroup_2)
        self.labelY_2.setObjectName("labelY_2")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelY_2)
        self.yPosition_target = QtWidgets.QDoubleSpinBox(parent=self.positionGroup_2)
        self.yPosition_target.setMinimum(-100.0)
        self.yPosition_target.setMaximum(100.0)
        self.yPosition_target.setSingleStep(0.1)
        self.yPosition_target.setObjectName("yPosition_target")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yPosition_target)
        self.follow_target_checkBox = QtWidgets.QCheckBox(parent=self.positionGroup_2)
        self.follow_target_checkBox.setObjectName("follow_target_checkBox")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.follow_target_checkBox)
        self.horizontalLayout_5.addWidget(self.positionGroup_2)
        self.arrayConfigGroup_4 = QtWidgets.QGroupBox(parent=self.arrayManagerContents_4)
        self.arrayConfigGroup_4.setObjectName("arrayConfigGroup_4")
        self.formLayout_11 = QtWidgets.QFormLayout(self.arrayConfigGroup_4)
        self.formLayout_11.setObjectName("formLayout_11")
        self.labelElements = QtWidgets.QLabel(parent=self.arrayConfigGroup_4)
        self.labelElements.setObjectName("labelElements")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelElements)
        self.numElements = QtWidgets.QSpinBox(parent=self.arrayConfigGroup_4)
        self.numElements.setMinimum(1)
        self.numElements.setMaximum(128)
        self.numElements.setProperty("value", 8)
        self.numElements.setObjectName("numElements")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.numElements)
        self.labelSpacing = QtWidgets.QLabel(parent=self.arrayConfigGroup_4)
        self.labelSpacing.setObjectName("labelSpacing")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelSpacing)
        self.elementSpacing = QtWidgets.QDoubleSpinBox(parent=self.arrayConfigGroup_4)
        self.elementSpacing.setDecimals(10)
        self.elementSpacing.setMinimum(1e-06)
        self.elementSpacing.setMaximum(10.0)
        self.elementSpacing.setSingleStep(0.1)
        self.elementSpacing.setProperty("value", 0.5)
        self.elementSpacing.setObjectName("elementSpacing")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.elementSpacing)
        self.labelCurvature = QtWidgets.QLabel(parent=self.arrayConfigGroup_4)
        self.labelCurvature.setObjectName("labelCurvature")
        self.formLayout_11.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelCurvature)
        self.curvature = QtWidgets.QDoubleSpinBox(parent=self.arrayConfigGroup_4)
        self.curvature.setMinimum(0.0)
        self.curvature.setMaximum(2.0)
        self.curvature.setSingleStep(0.1)
        self.curvature.setObjectName("curvature")
        self.formLayout_11.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.curvature)
        self.horizontalLayout_5.addWidget(self.arrayConfigGroup_4)
        self.positionGroup = QtWidgets.QGroupBox(parent=self.arrayManagerContents_4)
        self.positionGroup.setObjectName("positionGroup")
        self.formLayout_10 = QtWidgets.QFormLayout(self.positionGroup)
        self.formLayout_10.setObjectName("formLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_10.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.verticalLayout_2)
        self.labelX = QtWidgets.QLabel(parent=self.positionGroup)
        self.labelX.setObjectName("labelX")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelX)
        self.xPosition = QtWidgets.QDoubleSpinBox(parent=self.positionGroup)
        self.xPosition.setMinimum(-100.0)
        self.xPosition.setMaximum(100.0)
        self.xPosition.setSingleStep(0.1)
        self.xPosition.setObjectName("xPosition")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.xPosition)
        self.labelY = QtWidgets.QLabel(parent=self.positionGroup)
        self.labelY.setObjectName("labelY")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelY)
        self.yPosition = QtWidgets.QDoubleSpinBox(parent=self.positionGroup)
        self.yPosition.setMinimum(-100.0)
        self.yPosition.setMaximum(100.0)
        self.yPosition.setSingleStep(0.1)
        self.yPosition.setObjectName("yPosition")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.yPosition)
        self.labelRotation = QtWidgets.QLabel(parent=self.positionGroup)
        self.labelRotation.setObjectName("labelRotation")
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelRotation)
        self.rotationLayout = QtWidgets.QHBoxLayout()
        self.rotationLayout.setSpacing(0)
        self.rotationLayout.setObjectName("rotationLayout")
        self.rotation = QtWidgets.QSlider(parent=self.positionGroup)
        self.rotation.setMinimum(-90)
        self.rotation.setMaximum(90)
        self.rotation.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.rotation.setObjectName("rotation")
        self.rotationLayout.addWidget(self.rotation)
        self.rotationValue = QtWidgets.QLabel(parent=self.positionGroup)
        self.rotationValue.setLineWidth(0)
        self.rotationValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.rotationValue.setWordWrap(False)
        self.rotationValue.setIndent(0)
        self.rotationValue.setObjectName("rotationValue")
        self.rotationLayout.addWidget(self.rotationValue)
        self.label = QtWidgets.QLabel(parent=self.positionGroup)
        self.label.setLineWidth(0)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.rotationLayout.addWidget(self.label)
        self.formLayout_10.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.rotationLayout)
        self.horizontalLayout_5.addWidget(self.positionGroup)
        self.arrayList = QtWidgets.QListWidget(parent=self.arrayManagerContents_4)
        self.arrayList.setObjectName("arrayList")
        self.horizontalLayout_5.addWidget(self.arrayList)
        self.arrayManagerDock.setWidget(self.arrayManagerContents_4)
        self.verticalLayout_4.addWidget(self.arrayManagerDock)
        self.arrayButtonLayout_4 = QtWidgets.QHBoxLayout()
        self.arrayButtonLayout_4.setObjectName("arrayButtonLayout_4")
        self.addArrayButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.addArrayButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.addArrayButton.setObjectName("addArrayButton")
        self.arrayButtonLayout_4.addWidget(self.addArrayButton)
        self.removeArrayButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.removeArrayButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.removeArrayButton.setObjectName("removeArrayButton")
        self.arrayButtonLayout_4.addWidget(self.removeArrayButton)
        self.verticalLayout_4.addLayout(self.arrayButtonLayout_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(410, 680, 1101, 281))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.InterferenceMap = QtWidgets.QWidget(parent=self.horizontalLayoutWidget_2)
        self.InterferenceMap.setEnabled(True)
        self.InterferenceMap.setMinimumSize(QtCore.QSize(0, 0))
        self.InterferenceMap.setMaximumSize(QtCore.QSize(1000, 483))
        self.InterferenceMap.setObjectName("InterferenceMap")
        self.horizontalLayout_2.addWidget(self.InterferenceMap)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1390, 30, 231, 190))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.scenarioManagerDock = QtWidgets.QDockWidget(parent=self.verticalLayoutWidget)
        self.scenarioManagerDock.setMaximumSize(QtCore.QSize(524287, 200))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.scenarioManagerDock.setFont(font)
        self.scenarioManagerDock.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.scenarioManagerDock.setAllowedAreas(QtCore.Qt.DockWidgetArea.AllDockWidgetAreas)
        self.scenarioManagerDock.setObjectName("scenarioManagerDock")
        self.scenarioContents_3 = QtWidgets.QWidget()
        self.scenarioContents_3.setObjectName("scenarioContents_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scenarioContents_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scenarioGroup = QtWidgets.QGroupBox(parent=self.scenarioContents_3)
        self.scenarioGroup.setObjectName("scenarioGroup")
        self.scenarioLayout_3 = QtWidgets.QVBoxLayout(self.scenarioGroup)
        self.scenarioLayout_3.setObjectName("scenarioLayout_3")
        self.scenarioSelect = QtWidgets.QComboBox(parent=self.scenarioGroup)
        self.scenarioSelect.setObjectName("scenarioSelect")
        self.scenarioLayout_3.addWidget(self.scenarioSelect)
        self.scenarioButtonLayout = QtWidgets.QHBoxLayout()
        self.scenarioButtonLayout.setObjectName("scenarioButtonLayout")
        self.loadScenarioButton = QtWidgets.QPushButton(parent=self.scenarioGroup)
        self.loadScenarioButton.setObjectName("loadScenarioButton")
        self.scenarioButtonLayout.addWidget(self.loadScenarioButton)
        self.saveScenarioButton = QtWidgets.QPushButton(parent=self.scenarioGroup)
        self.saveScenarioButton.setObjectName("saveScenarioButton")
        self.scenarioButtonLayout.addWidget(self.saveScenarioButton)
        self.scenarioLayout_3.addLayout(self.scenarioButtonLayout)
        self.verticalLayout_9.addWidget(self.scenarioGroup)
        self.scenarioManagerDock.setWidget(self.scenarioContents_3)
        self.verticalLayout_19.addWidget(self.scenarioManagerDock)
        self.horizontalLayout_6.addWidget(self.widget)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1650, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.beamControlDock.setWindowTitle(_translate("MainWindow", "Beam Control"))
        self.beamControlGroup.setTitle(_translate("MainWindow", "Beam Control"))
        self.labelSteering.setText(_translate("MainWindow", "Steering Angle:"))
        self.steeringValue.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "°"))
        self.comboBox.setItemText(0, _translate("MainWindow", "acoustic"))
        self.comboBox.setItemText(1, _translate("MainWindow", "electormagnitic"))
        self.frequencyListGroup.setTitle(_translate("MainWindow", "Frequency components"))
        self.label_3.setText(_translate("MainWindow", "Frequency"))
        self.label_4.setText(_translate("MainWindow", "Amplitude"))
        self.label_5.setText(_translate("MainWindow", "Phase"))
        self.addFrequencyButton.setText(_translate("MainWindow", "Add"))
        self.removeFrequencyButton.setText(_translate("MainWindow", "Remove"))
        self.arrayManagerDock.setWindowTitle(_translate("MainWindow", "Array Manager"))
        self.positionGroup_2.setTitle(_translate("MainWindow", "Array Target"))
        self.labelX_2.setText(_translate("MainWindow", "X Position:"))
        self.labelY_2.setText(_translate("MainWindow", "Y Position:"))
        self.follow_target_checkBox.setText(_translate("MainWindow", "Follow target"))
        self.arrayConfigGroup_4.setTitle(_translate("MainWindow", "Array Configuration"))
        self.labelElements.setText(_translate("MainWindow", "Elements:"))
        self.labelSpacing.setText(_translate("MainWindow", "Spacing:"))
        self.labelCurvature.setText(_translate("MainWindow", "Curvature:"))
        self.positionGroup.setTitle(_translate("MainWindow", "Position and Rotation"))
        self.labelX.setText(_translate("MainWindow", "X Position:"))
        self.labelY.setText(_translate("MainWindow", "Y Position:"))
        self.labelRotation.setText(_translate("MainWindow", "Rotation (°):"))
        self.rotationValue.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "°"))
        self.addArrayButton.setText(_translate("MainWindow", "Add Array"))
        self.removeArrayButton.setText(_translate("MainWindow", "Remove Array"))
        self.scenarioManagerDock.setWindowTitle(_translate("MainWindow", "Scenario Manager"))
        self.scenarioGroup.setTitle(_translate("MainWindow", "Scenario"))
        self.loadScenarioButton.setText(_translate("MainWindow", "Load"))
        self.saveScenarioButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
