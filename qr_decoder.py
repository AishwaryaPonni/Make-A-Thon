from picamera import PiCamera
from time import sleep
from qrtools import QR
camera = PiCamera()

import RPi.GPIO as GPIO
import time

sensor = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)



print "IR Sensor Ready....."
print " "

try: 
   while True:
      if GPIO.input(sensor):
          print "No Ob"  
 #         GPIO.setup(18,GPIO.OUT)
#          GPIO.output(18,GPIO.HIGH)
      else: 
          print "Object Detected" 
          time.sleep(0.2)

          camera.start_preview
          sleep(1)
	  camera.capture('/tmp/picture.jpg')
	  camera.stop_preview
          my_QR=QR(filename="/tmp/picture.jpg")
	  my_QR.decode()
 	  print(my_QR.data)
	  if(my_QR.data=="Room1"):
		print "Door Opening"
                GPIO.setup(17,GPIO.OUT)
	  	print "LED ON"
 	        GPIO.output(17,GPIO.HIGH)
	        time.sleep(1)
	        GPIO.output(17,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
