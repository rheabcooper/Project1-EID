#!/usr/bin/python
#Reference:https://github.com/adafruit/Adafruit_Python_DHT and https://www.tutorialspoint.com/pyqt/pyqt_basic_widgets.htm



import sys 
import time 
import Adafruit_DHT 
import datetime 
import PyQt4 
from PyQt4 import QtCore, QtGui,uic 
from A import Ui_MainWindow        
#importing required modules to plot graph
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

class MyMainWindow(QtGui.QMainWindow):
    """main class that contains all the methods required for the GUI""" 
 
    def __init__(self, parent=None):
        """constructor of class"""
	QtGui.QWidget.__init__(self, parent)
	self.ui = Ui_MainWindow()
	self.ui.setupUi(self)
	self.ui.showhum_button.clicked.connect(self.Start)  #connecting the push buttons to methods
	self.ui.Humgraph_button.clicked.connect(self.HumGraph)
	self.ui.Tempgraph_button.clicked.connect(self.TempGraph)
	self.ui.close_button.clicked.connect(self.close)
	self.ui.showaverage_button.clicked.connect(self.ShowAverage)
	self.ui.figure=plt.figure(figsize=(15,5))
	self.ui.canvas=FigureCanvas(self.ui.figure)
	self.ui.gridLayout.addWidget(self.ui.canvas,1,0,1,2)
  	self.ui.cb.currentIndexChanged.connect(self.Select)  
        self.ui.iterations = 5     #default number of iterations 
   
    def Select(self,item):
	"""method to update the number of iterations with the selected value from the combo box"""
        if item == 0:
	   self.ui.iterations=5
	if item == 1:
	   self.ui.iterations=10
	if item == 2:
	   self.ui.iterations=15
	
    def ShowAverage(self):
        """Method to display average of the temp and humidity lists in a dialog box that pops up when the button is pressed"""
	averagehum=sum(a)/len(a)
	averagetemp=sum(b)/len(b)
	showavghum="Average Humidity is " + str(averagehum)
	showavgtemp="\nAverage Temperature is " + str(averagetemp)
	d=QtGui.QDialog()
	d.setWindowTitle("Average")
	l2=QtGui.QLabel(d)
	l2.setText(showavghum + showavgtemp)
	l2.show()
	d.exec_()             
        
    def TempGraph(self):
        """graph plotting Referenced from a youtube video :https://www.youtube.com/watch?v=Wk7CECwebMc"""
 	plt.cla()
	ax=self.ui.figure.add_subplot(111)
	x=[i for i in range(len(b))]  #iterations on x axis
	y=b                            #temperature values on y axis
	ax.plot(x,y,'b.-')
	ax.set_title('Temperature')
	self.ui.canvas.draw()

    def HumGraph(self):
        """graph plotting Referenced from a youtube video :https://www.youtube.com/watch?v=Wk7CECwebMc"""
        plt.cla()
        ax=self.ui.figure.add_subplot(111)
        x=[i for i in range(len(a))]           #iterations on x axis
        y=a					#humidity list values on y axis
        ax.plot(x,y,'b.-')
        ax.set_title('Humidity')
        self.ui.canvas.draw()
    	
    def Start(self):
        """this method gets the temp, humidity values one by one, displays them along with timestamp and also populates a list that pops up when a predefined number of iterations is done"""
	listWidget=QtGui.QListWidget()
	listWidget.setWindowTitle("List of Values")
	for i in range(self.ui.iterations):
            humidity,temperature = Adafruit_DHT.read_retry(sensor, pin)
	    a.append(humidity)
	    b.append(temperature)
	    if temperature and humidity is not None :
	       showtemp="Temperature is in degree Celsius is " + str(temperature) 
	       showhum="\nHumidity is : " + str(humidity)
	       now = datetime.datetime.now() 
	       showtime="\nCurrent time is : " + now.strftime("%Y-%m-%d %H:%M:%S") 
	       self.ui.showhum_window.setText(showtemp + showhum + showtime)
	       item=QtGui.QListWidgetItem("Temp: %f , Humidity: %f " % (temperature,humidity))
               listWidget.addItem(item)
 # a message box with a warning acts as an alarm when temperature crosses a predefined threshold"""
	       if temperature > threshold: 
                  w=QtGui.QWidget()
                  result=QtGui.QMessageBox.warning(w, "Message", "Temperature too high")
               else:
		  self.ui.statusbar.showMessage("Temperature optimal",1000000)
            else:      #handling not receiving data
               shownotemp="Sorry, temperature , humidity unavailable . Try again ";
               self.ui.showhum_window.setText(shownotemp)
            time.sleep(2) 
	listWidget.show()
	listWidget.exec_()

#Reference: https://github.com/adafruit/Adafruit_Python_DHT
# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

a=[]     #humidity list
b=[]     #temperature list
threshold=30       #threshold for temperature

#instantiating the above class
app=QtGui.QApplication(sys.argv)
myapp=MyMainWindow()
myapp.show()
sys.exit(app.exec_())

