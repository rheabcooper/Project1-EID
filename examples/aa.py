import sys

import PyQt4 
from PyQt4 import QtCore, QtGui,uic
from tax_aaaa import Ui_MainWindow


class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
	QtGui.QWidget.__init__(self, parent)
	self.ui = Ui_MainWindow()
	self.ui.setupUi(self)

if __name__== "__main__":
        app=QtGui.QApplication(sys.argv)
	myapp=MyMainWindow()
	myapp.show()
	sys.exit(app.exec_())


