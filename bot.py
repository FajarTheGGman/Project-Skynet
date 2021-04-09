import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

def control(pin, angle):
    GPIO.setup(pin, GPIO.OUT)
    x = GPIO.PWM(pin, 50)
    x.start(2)
    x.ChangeDutyCycle(angle)
    time.sleep(2)
    x.stop()
    GPIO.cleanup()

control(int(sys.argv[1]), int(sys.argv[2]))
