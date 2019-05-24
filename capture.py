from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (480, 320)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480,320))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port= True):
    image = frame.array

    cv2.imshow('Frame', image)
    key = cv2.waitKey(1)&0xff
    rawCapture.truncate(0)
    if key == 27:
        break

rawCapture.release()
cv2.destroyAllWindows()
