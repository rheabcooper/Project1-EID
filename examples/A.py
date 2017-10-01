# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A.ui'
#
# Created: Sat Sep 30 15:47:42 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(578, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../pi.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.showhum_button = QtGui.QPushButton(self.centralwidget)
        self.showhum_button.setGeometry(QtCore.QRect(10, 10, 251, 61))
        self.showhum_button.setObjectName(_fromUtf8("showhum_button"))
        self.showhum_window = QtGui.QTextEdit(self.centralwidget)
        self.showhum_window.setGeometry(QtCore.QRect(280, 10, 281, 81))
        self.showhum_window.setObjectName(_fromUtf8("showhum_window"))
        self.close_button = QtGui.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(340, 130, 81, 21))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.showaverage_button = QtGui.QPushButton(self.centralwidget)
        self.showaverage_button.setGeometry(QtCore.QRect(20, 80, 181, 31))
        self.showaverage_button.setObjectName(_fromUtf8("showaverage_button"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 170, 541, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.HumGraph_button = QtGui.QPushButton(self.centralwidget)
        self.HumGraph_button.setGeometry(QtCore.QRect(20, 130, 121, 31))
        self.HumGraph_button.setObjectName(_fromUtf8("HumGraph_button"))
        self.TempGraph_button = QtGui.QPushButton(self.centralwidget)
        self.TempGraph_button.setGeometry(QtCore.QRect(170, 130, 151, 31))
        self.TempGraph_button.setObjectName(_fromUtf8("TempGraph_button"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Project1", None))
        self.showhum_button.setText(_translate("MainWindow", "Current Humidity and Temperature", None))
        self.close_button.setText(_translate("MainWindow", "Close", None))
        self.showaverage_button.setText(_translate("MainWindow", "Click to get Average ", None))
        self.HumGraph_button.setText(_translate("MainWindow", "Humidity Graph", None))
        self.TempGraph_button.setText(_translate("MainWindow", "Temperature Graph", None))

