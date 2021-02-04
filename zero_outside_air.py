#Python progam to run a Cozir Sensor by JTH 01/17/2018
import serial
import time
 
ser = serial.Serial("/dev/ttyUSB0")
print "Python Progam for Cozir Ambient Sensor Development Kit"

# \r\n is CR and LF
ser.flushInput()
time.sleep(1)

ser.write("G\r\n")
print "Output - " + ser.read(10)



