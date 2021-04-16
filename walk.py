import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(sys.argv[1]), GPIO.OUT)

x = GPIO.PWM(int(sys.argv[1]), 50)

x.start(5)

def minimum():
    for i in range(2, 4):
        x.ChangeDutyCycle(i)
        time.sleep(0.5)

    for d in range(4, 2):
        x.ChangeDutyCycle(d)
        time.sleep(0.5)

    x.stop()
    GPIO.cleanup()

def maximum():
    for i in range(10, 12):
        x.ChangeDutyCycle(i)
        time.sleep(0.5)

    for d in range(12, 10):
        x.ChangeDutyCycle(d)
        time.sleep(0.5)

    x.stop()
    GPIO.cleanup()

pin = int(sys.argv[1])

if pin == 3:
    minimum()
elif pin == 5:
    minimum()
elif pin == 17:
    maximum()
elif pin == 13:
    maximum()
else:
    print('Error')
