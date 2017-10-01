# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tax.ui'
#
# Created: Fri Sep 22 15:25:25 2017
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
        self.MainBox = QtGui.QWidget(MainWindow)
        self.MainBox.setObjectName(_fromUtf8("MainBox"))
        self.price_box = QtGui.QTextEdit(self.MainBox)
        self.price_box.setGeometry(QtCore.QRect(210, 140, 211, 261))
        self.price_box.setObjectName(_fromUtf8("price_box"))
        self.price = QtGui.QLabel(self.MainBox)
        self.price.setGeometry(QtCore.QRect(120, 180, 67, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.price.setFont(font)
        self.price.setObjectName(_fromUtf8("price"))
        self.tax_rate = QtGui.QSpinBox(self.MainBox)
        self.tax_rate.setGeometry(QtCore.QRect(110, 250, 64, 33))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName(_fromUtf8("tax_rate"))
        self.calc_tax_button = QtGui.QPushButton(self.MainBox)
        self.calc_tax_button.setGeometry(QtCore.QRect(230, 430, 101, 31))
        self.calc_tax_button.setObjectName(_fromUtf8("calc_tax_button"))
        MainWindow.setCentralWidget(self.MainBox)
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
        self.price.setText(_translate("MainWindow", "Price", None))
        self.calc_tax_button.setText(_translate("MainWindow", "Calculate Tax", None))

