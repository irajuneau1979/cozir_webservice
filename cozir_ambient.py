#Python progam to run a Cozir Sensor by JTH 01/17/2018
import serial
import time
import json
import requests

ser = serial.Serial("/dev/ttyUSB0")
print "Python Progam for Cozir Ambient Sensor Development Kit"

# \r\n is CR and LF
ser.flushInput()
time.sleep(1)

headers = {
	"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmYmM0MTE5NGM3YTk0NmViYmIxNzdkOWI3OTI1NWViYiIsImlhdCI6MTU5NTA5Njg1OCwiZXhwIjoxOTEwNDU2ODU4fQ.DJ20YW1_L-QH_2UZu2C0B6DAWpNssZffoc_xpdvXkbI",
	"content-type": "application/json"
}

ser.write("Z\r\n")
resp = ser.read(10)
resp = resp[:8]
fltCo2 = float(resp[2:])
print "CO2 PPM  =", fltCo2 * 1 # multiplierZ

payload = {
    'state': fltCo2
}

requests.post("http://127.0.0.1:8123/api/states/variable.baby_room_co2", data=json.dumps(payload), headers=headers)


