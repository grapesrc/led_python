import RPi.GPIO as GPIO
import time

GPIO_PIN = 3
GPIO.setup(GPIO_PIN,GPIO.OUT)
while True:
	GPIO.output(GPIO_PIN,True)
	time.sleep(2)
	GPIO.output(GPIO_PIN,False)
	time.sleep(2)
GPIO.cleanup()