#Python progam to run a Cozir Sensor by JTH 01/17/2018
import serial
import time
 
ser = serial.Serial("/dev/ttyUSB0")
print "Python Progam for Cozir Ambient Sensor Development Kit"

# \r\n is CR and LF
ser.flushInput()
time.sleep(1)

while True:
    ser.write("Z\r\n")
    resp = ser.read(10)
    resp = resp[:8]
    fltCo2 = float(resp[2:])
    print "CO2 PPM  =", fltCo2 * .5 # multiplierZ
    time.sleep(1)

