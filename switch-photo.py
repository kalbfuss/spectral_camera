#!/usr/bin/python


import os,sys
import csv
import time
import RPi.GPIO as GPIO

switch = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.OUT)
try:
    while True:
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        str = 'raspistill -o ./pictures/'+now+ 'A.jpg'
        GPIO.output(switch,GPIO.HIGH)
        os.system(str)
#        time.sleep(5)
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        str = 'raspistill -o ./pictures/'+now+ 'B.jpg'
        GPIO.output(switch,GPIO.LOW)
        os.system(str)
        time.sleep(3)
except:
    print("except")
GPIO.cleanup()


