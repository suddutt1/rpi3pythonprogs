#Libraries
import RPi.GPIO as GPIO
import time
import thread
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER = 38
GPIO_ECHO = 40
GPIO_RED = 7
GPIO_GREEN = 3 
GPIO_AMBER= 5
_running=False
_flashingLED=GPIO_GREEN
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_RED, GPIO.OUT)
GPIO.setup(GPIO_GREEN, GPIO.OUT)
GPIO.setup(GPIO_AMBER, GPIO.OUT)

def keep_blinking():
   global _flashingLED
   global _running
   GPIO.output(GPIO_RED,False) 
   GPIO.output(GPIO_GREEN,False)
   GPIO.output(GPIO_AMBER,False)
   _running = True
   while _running == True:
      GPIO.output(GPIO_RED,False)
      GPIO.output(GPIO_GREEN,False)
      GPIO.output(GPIO_AMBER,False)
      GPIO.output(_flashingLED,True)
      time.sleep(0.05)
      GPIO.output(_flashingLED,False)
      time.sleep(0.05)
     
def alarm(distance):
    global _flashingLED
    if distance < 20 :
        print("Very near %.2f cm" % distance)
        _flashingLED = GPIO_RED
    elif distance >=20 and distance <100:
        print("Not so near %.2f cm" % distance)
        _flashingLED=GPIO_AMBER
    else:
       print("Far away %.2f cm" % distance)
       _flashingLED = GPIO_GREEN
    return 

     
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        thread.start_new_thread(keep_blinking, ())
        while True:
            dist = distance()
            #print ("Measured Distance = %.1f cm" % dist)
            alarm(dist)
	    time.sleep(1)
                      
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        _running=False
        GPIO.cleanup()
