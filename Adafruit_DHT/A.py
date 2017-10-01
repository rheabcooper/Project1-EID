# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A.ui'
#
# Created: Sun Sep 24 14:26:58 2017
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.title = QtGui.QTextEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(180, 30, 431, 51))
        self.title.setObjectName(_fromUtf8("title"))
        self.showtemp_button = QtGui.QPushButton(self.centralwidget)
        self.showtemp_button.setGeometry(QtCore.QRect(50, 120, 191, 71))
        self.showtemp_button.setObjectName(_fromUtf8("showtemp_button"))
        self.showhum_button = QtGui.QPushButton(self.centralwidget)
        self.showhum_button.setGeometry(QtCore.QRect(50, 270, 191, 71))
        self.showhum_button.setObjectName(_fromUtf8("showhum_button"))
        self.showtemp_window = QtGui.QTextEdit(self.centralwidget)
        self.showtemp_window.setGeometry(QtCore.QRect(290, 120, 431, 111))
        self.showtemp_window.setObjectName(_fromUtf8("showtemp_window"))
        self.showhum_window = QtGui.QTextEdit(self.centralwidget)
        self.showhum_window.setGeometry(QtCore.QRect(290, 270, 431, 131))
        self.showhum_window.setObjectName(_fromUtf8("showhum_window"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.title.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:12pt; font-weight:200; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Project 1</p></body></html>", None))
        self.showtemp_button.setText(_translate("MainWindow", "Click to get Temperature", None))
        self.showhum_button.setText(_translate("MainWindow", "Click to get Humidity", None))

