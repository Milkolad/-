#!/usr/bin/env python3
from picamera import PiCamera
from time import sleep
import keyboard

name=input()
di="/home/pi/Documents/camera/foto/"
ras=".h264"
directory=di+name+ras

camera = PiCamera()
camera.start_preview()
camera.start_recording(directory)
while True:
        if keyboard.is_pressed('o'):
            camera.stop_recording()
            camera.stop_preview()
            break
#sleep(10)