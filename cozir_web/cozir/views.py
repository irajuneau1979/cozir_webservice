# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import JsonResponse

#Python progam to run a Cozir Sensor by JTH 01/17/2018
import serial
import time

from django.shortcuts import render

def cozir_val(request):
   ser = serial.Serial("/dev/ttyUSB0")

   # \r\n is CR and LF
   ser.flushInput()
   time.sleep(1)

   ser.write("Z\r\n".encode())
   resp = ser.read(10)
   resp = resp[:8]
   fltCo2 = float(resp[2:])

   data = {
     'co2': fltCo2
   }

   return JsonResponse(data)

def cozir_reset(request):
   ser = serial.Serial("/dev/ttyUSB0")

   ser.flushInput()
   time.sleep(1)

   ser.write("G\r\n".encode())

   return HttpResponse("Reset " + ser.read(10))

# Create your views here.
