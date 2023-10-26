from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.start_preview()
#camera.resolution=(600,900)
camera.vflip=True
#camera.hflip=True
sleep(10)
camera.capture('/home/pi/Desktop/test_d.jpg')
camera.stop_preview()
