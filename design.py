# Form implementation generated from reading ui file 'app-ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 296)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 80, 161, 80))
        self.widget.setObjectName("widget")
        self.labelMax = QtWidgets.QLabel(parent=self.widget)
        self.labelMax.setGeometry(QtCore.QRect(10, 50, 21, 17))
        self.labelMax.setObjectName("labelMax")
        self.minValue = QtWidgets.QLineEdit(parent=self.widget)
        self.minValue.setGeometry(QtCore.QRect(40, 10, 113, 25))
        self.minValue.setObjectName("minValue")
        self.maxValue = QtWidgets.QLineEdit(parent=self.widget)
        self.maxValue.setGeometry(QtCore.QRect(40, 50, 113, 25))
        self.maxValue.setObjectName("maxValue")
        self.labelMin = QtWidgets.QLabel(parent=self.widget)
        self.labelMin.setGeometry(QtCore.QRect(10, 10, 21, 17))
        self.labelMin.setObjectName("labelMin")
        self.themeBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.themeBox.setGeometry(QtCore.QRect(20, 30, 361, 31))
        self.themeBox.setObjectName("themeBox")
        self.selectDir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.selectDir.setGeometry(QtCore.QRect(590, 40, 131, 31))
        self.selectDir.setObjectName("selectDir")
        self.currentDir = QtWidgets.QLabel(parent=self.centralwidget)
        self.currentDir.setGeometry(QtCore.QRect(440, 90, 421, 17))
        self.currentDir.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.currentDir.setObjectName("currentDir")
        self.startBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(40, 200, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор примеров"))
        self.labelMax.setText(_translate("MainWindow", "До"))
        self.minValue.setText(_translate("MainWindow", "10"))
        self.maxValue.setText(_translate("MainWindow", "100"))
        self.labelMin.setText(_translate("MainWindow", "От"))
        self.themeBox.setPlaceholderText(_translate("MainWindow", "Выберите тему"))
        self.selectDir.setText(_translate("MainWindow", "Выберите папку"))
        self.currentDir.setText(_translate("MainWindow", "Папка не выбрана"))
        self.startBtn.setText(_translate("MainWindow", "START 🔥"))