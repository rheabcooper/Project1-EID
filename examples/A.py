# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A.ui'
#
# Created: Sun Oct  1 12:05:05 2017
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
        MainWindow.resize(601, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../pi.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.showhum_button = QtGui.QPushButton(self.centralwidget)
        self.showhum_button.setGeometry(QtCore.QRect(10, 10, 251, 61))
        self.showhum_button.setObjectName(_fromUtf8("showhum_button"))
        self.showhum_window = QtGui.QTextEdit(self.centralwidget)
        self.showhum_window.setGeometry(QtCore.QRect(280, 0, 281, 71))
        self.showhum_window.setObjectName(_fromUtf8("showhum_window"))
        self.close_button = QtGui.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(200, 90, 81, 21))
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.showaverage_button = QtGui.QPushButton(self.centralwidget)
        self.showaverage_button.setGeometry(QtCore.QRect(10, 80, 181, 31))
        self.showaverage_button.setObjectName(_fromUtf8("showaverage_button"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 210, 541, 181))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Humgraph_button = QtGui.QPushButton(self.centralwidget)
        self.Humgraph_button.setGeometry(QtCore.QRect(20, 130, 121, 31))
        self.Humgraph_button.setObjectName(_fromUtf8("Humgraph_button"))
        self.Tempgraph_button = QtGui.QPushButton(self.centralwidget)
        self.Tempgraph_button.setGeometry(QtCore.QRect(150, 130, 151, 31))
        self.Tempgraph_button.setObjectName(_fromUtf8("Tempgraph_button"))
        self.cb = QtGui.QComboBox(self.centralwidget)
        self.cb.setGeometry(QtCore.QRect(340, 130, 85, 31))
        self.cb.setObjectName(_fromUtf8("cb"))
        self.cb.addItem(_fromUtf8(""))
        self.cb.addItem(_fromUtf8(""))
        self.cb.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 80, 211, 31))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 27))
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
        self.Humgraph_button.setText(_translate("MainWindow", "Humidity Graph", None))
        self.Tempgraph_button.setText(_translate("MainWindow", "Temperature Graph", None))
        self.cb.setItemText(0, _translate("MainWindow", "5", None))
        self.cb.setItemText(1, _translate("MainWindow", "10", None))
        self.cb.setItemText(2, _translate("MainWindow", "15", None))
        self.label.setText(_translate("MainWindow", "Change number of Iterations:", None))

