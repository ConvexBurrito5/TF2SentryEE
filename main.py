import os
import struct
import time

import board
import digitalio
import busio
from motorcontrollerft232h import MotorControllerFT232H
from board import SDA, SCL
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from threading import Event

usb = MotorControllerFT232H()
time.sleep(1)
usb.setXAngle(0)
usb.setYAngle(0)
time.sleep(1)

event = Event()


while True:

    print("X Pos: {}, Y Pos: {}".format(usb.getXAngle(), usb.getYAngle()))
    usb.idle(event)
    time.sleep(5)
    event.set()



    '''
    usb.set_xAngle(270)
    usb.set_yAngle(180)
    time.sleep(.75)
    usb.set_xAngle(0)
    usb.set_yAngle(0)
    time.sleep(2)
    '''
    '''
    usb.set_xAngle(120)
    usb.set_yAngle(120)
    time.sleep(.2)
    usb.set_xAngle(80)
    usb.set_yAngle(80)
    time.sleep(.2)
    usb.pauseMovement()
    time.sleep(.2)
    usb.set_xAngle(90)
    usb.set_xAngle(90)
    '''