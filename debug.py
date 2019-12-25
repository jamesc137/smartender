import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# Orange
GPIO.setup(17, GPIO.OUT)
# Green
GPIO.setup(27, GPIO.OUT)
# Yellow
GPIO.setup(22, GPIO.OUT)
# Purple
GPIO.setup(23, GPIO.OUT)
# Gray
GPIO.setup(24, GPIO.OUT)
# White
GPIO.setup(25, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)

# Orange
GPIO.output(17, GPIO.LOW)
time.sleep(5)
GPIO.output(17, GPIO.HIGH)
time.sleep(1)
# Green
GPIO.output(27, GPIO.LOW)
time.sleep(5)
GPIO.output(27, GPIO.HIGH)
time.sleep(1)
# Yellow
GPIO.output(22, GPIO.LOW)
time.sleep(5)
GPIO.output(22, GPIO.HIGH)
time.sleep(1)
# Purple
GPIO.output(23, GPIO.LOW)
time.sleep(5)
GPIO.output(23, GPIO.HIGH)
time.sleep(1)
# Gray
GPIO.output(24, GPIO.LOW)
time.sleep(5)
GPIO.output(24, GPIO.HIGH)
time.sleep(1)

# White
GPIO.output(25, GPIO.LOW)
time.sleep(5)
GPIO.output(25, GPIO.HIGH)
time.sleep(1)

GPIO.cleanup()