from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import time
import datetime

camera = PiCamera()
camera.resolution = (480, 360)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480,360))

now = datetime.datetime.now()

filename = now.strftime('%Y -%m -%d %H:%M:%S')
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port= True):
    image = frame.array

    cv2.imwrite('./'+filename+'.jpg',image)
    break;
    key = cv2.waitKey(1)&0xff
    rawCapture.truncate(0)
    if key == 27:
        break

cv2.destroyAllWindows()

