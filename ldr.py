import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
GPIO.setup(10, GPIO.OUT)

def ldr():
    while True:
        if GPIO.input(22):
            GPIO.output(10, 1)
            GPIO.cleanup()
        else:
            GPIO.output(10, 0)
            GPIO.cleanup()

ldr()

