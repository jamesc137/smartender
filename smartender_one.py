import time
import json
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

# Make a cocktail
with open("recipes.json", "r+") as jsonFile:
    data = json.load(jsonFile)
    
drink = raw_input("Enter: ")

ingredient1 = list(data['drinks'][0]['ingredients'][0].values())[0]
ingredient2 = list(data['drinks'][0]['ingredients'][1].values())[0]

    
GPIO.output(17, GPIO.LOW)
time.sleep(ingredient1)
GPIO.output(17, GPIO.HIGH)

GPIO.output(22, GPIO.LOW)
time.sleep(ingredient2)
GPIO.output(22, GPIO.HIGH)


GPIO.cleanup()
