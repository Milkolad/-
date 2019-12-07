#!/usr/bin/env python3
from picamera import PiCamera
from time import sleep


name=input()
di="/home/pi/Documents/camera/foto/"
ras=".jpg"
directory=di+name+ras

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture(directory)
camera.stop_preview()