Local QT-Based UI -Rhea Cooper
==================================
The first Project of ECEN 5053-002 : Embedded Interface Design involves developing a GUI using QT on RaspberryPi to help retrieve humidity and temperature values from the DHT22 sensor 


Installation Instructions
==================================
1.Install all the python libraries.
2.Install PyQt4
3.Install matplotlib
4.Connect the DHT22 to GPIO4 of the RaspberryPi with a 4.7k or 10k resistor
5.In the example folder run : sudo ./AdafruitDHT.py 22 4

Project Work
==================================
Temperature and Humidity values are displayed on the GUI when the user requests them along with the timestamp. A message is displayed if no values are available.

Project Additions:
==================================
1.A message box shows up with a warning if the temperature rises above a pre-defined threshold
2.Lists get populated simultaneously when the user requests temperature and humidity values which are displayed on the GUI in a dialog box when a specified number of iterations are over.
3.The average of humidity and temperature values in the list is displayed in a dialog box when the user presses the corresponding pushbutton.
4.The number of iterations in the loop or the number values retrieved by the sensor can be changed by the user with the help of a drop-down menu (QComboBox)
5.Temperature and humidity plots are displayed when the corresponding push buttons are clicked when the corresponding push buttons are clicked.
