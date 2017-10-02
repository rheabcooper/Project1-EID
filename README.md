Local QT-Based UI -Rhea Cooper
==================================
Repository for the first Project of ECEN 5053-002 : Embedded Interface Design which involves developing a prototype of a standalone temperature monitoring device with a local user-interface (QT).
QT is used on RaspberryPi to help retrieve humidity and temperature values from the DHT22 sensor.  

Author: Rhea Cooper

Date: 10/1/2017

Installation Instructions
==================================
1.Install all the python libraries and dependencies :
``````````````````````````````````````````````````````````` 
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl
sudo python setup.py install
`````````````````````````````````````````````````````````````             
2.Install QT4 designer :
```````````````````````````````````````````````````````````
sudo apt-get install qt4-designer
```````````````````````````````````````````````````````````
3.Install PyQt4 : 
```````````````````````````````````````````````````````````
sudo apt-get install pyqt4
```````````````````````````````````````````````````````````
4.Install matplotlib : 
```````````````````````````````````````````````````````````
sudo apt-get install python-matplotlib
```````````````````````````````````````````````````````````
5.Connect the DHT22 to GPIO4 of the RaspberryPi with a 4.7k or 10k resistor

6.In the example folder run :
```````````````````````````````````````````````````````````
sudo ./AdafruitDHT.py 22 4
```````````````````````````````````````````````````````````


Project Work
==================================

Temperature and Humidity values are displayed on the GUI when the user requests them along with the timestamp. A message is displayed if no values are available.


Project Additions:
==================================
1.A message box shows up with a warning if the temperature rises above a pre-defined threshold.

2.Lists get populated simultaneously when the user requests temperature and humidity values. The collection of values is displayed on the GUI in a dialog box when a specified number of iterations are over.

3.The average of humidity and temperature values in the list is displayed in a dialog box when the user presses the corresponding pushbutton.

4.The number of iterations in the loop or the number values retrieved by the sensor can be changed by the user with the help of a drop-down menu (QComboBox).

5.Temperature and humidity plots are displayed when the corresponding push buttons are clicked.


References
==================================
1.https://github.com/adafruit/Adafruit_Python_DHT.git
2.https://www.tutorialspoint.com/pyqt/pyqt_basic_widgets.htm
3.https://pythonspot.com/en/pyqt4-gui-tutorial/
4.http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/
5.https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/overview 
