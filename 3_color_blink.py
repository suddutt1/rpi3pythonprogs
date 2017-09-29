import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(3, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
try:

	while True:
		print("Start blinking")
        	GPIO.output(3,True)  ## Turn on Led
 		time.sleep(0.1)
		GPIO.output(3,False)
		GPIO.output(5,True)
		time.sleep(0.1)
		GPIO.output(5,False)
 		GPIO.output(7,True)
		time.sleep(0.1)         ## Wait for one second
		#GPIO.output(3,False) ## Turn off Led
 		#GPIO.output(5,False)
 		GPIO.output(7,False)
		time.sleep(0.1)         ## Wait for one second
		print("Stop blinking")
except KeyboardInterrupt:  
		print("Stopping now")
finally:
	GPIO.output(3,False)
	GPIO.output(5,False)
	GPIO.output(7,False)
	GPIO.cleanup()
