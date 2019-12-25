from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import StringProperty

import json
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

class Bartender():
    def __init__(self):
        GPIO.cleanup()

class Main(TabbedPanel):

    # Setup Pumps based on pump_config.json
    def configure_pumps():
    	pump_configuration = json.load(open('pump_config.json'))
    	for pump in self.pump_configuration.keys():
    		GPIO.setup(self.pump_configuration[pump]["pin"], GPIO.OUT, initial=GPIO.HIGH)

    # Show Menu Items
    with open("recipes.json", "r") as jsonFile:
        data = json.load(jsonFile)

    # Make Drink
    def make_drink(self, drink):
        with open("recipes.json", "r+") as jsonFile:
            data = json.load(jsonFile)

        if drink == "rum_and_coke":
            ingredient1 = list(data['drinks'][0]['ingredients'][0].values())[0]
            ingredient2 = list(data['drinks'][0]['ingredients'][1].values())[0]
            GPIO.output(17, GPIO.LOW)
            time.sleep(ingredient1)
            GPIO.output(17, GPIO.HIGH)

            GPIO.output(22, GPIO.LOW)
            time.sleep(ingredient2)
            GPIO.output(22, GPIO.HIGH)
            
        if drink == "screw_driver":
            ingredient1 = list(data['drinks'][0]['ingredients'][0].values())[0]
            ingredient2 = list(data['drinks'][0]['ingredients'][1].values())[0]
            GPIO.output(17, GPIO.LOW)
            time.sleep(ingredient1)
            GPIO.output(17, GPIO.HIGH)

            GPIO.output(22, GPIO.LOW)
            time.sleep(ingredient2)
            GPIO.output(22, GPIO.HIGH)

        if drink == "screw_driver":
            ingredient1 = list(data['drinks'][0]['ingredients'][0].values())[0]
            ingredient2 = list(data['drinks'][0]['ingredients'][1].values())[0]
            GPIO.output(17, GPIO.LOW)
            time.sleep(ingredient1)
            GPIO.output(17, GPIO.HIGH)

            GPIO.output(22, GPIO.LOW)
            time.sleep(ingredient2)
            GPIO.output(22, GPIO.HIGH)
            
        if drink == "mimosa":
            ingredient1 = list(data['drinks'][0]['ingredients'][0].values())[0]
            ingredient2 = list(data['drinks'][0]['ingredients'][1].values())[0]
            GPIO.output(17, GPIO.LOW)
            time.sleep(ingredient1)
            GPIO.output(17, GPIO.HIGH)

            GPIO.output(22, GPIO.LOW)
            time.sleep(ingredient2)
            GPIO.output(22, GPIO.HIGH)
            
        if drink == "tequila_sunrise":
            ingredient1 = list(data['drinks'][0]['ingredients'][0].values())[0]
            ingredient2 = list(data['drinks'][0]['ingredients'][1].values())[0]
            GPIO.output(17, GPIO.LOW)
            time.sleep(ingredient1)
            GPIO.output(17, GPIO.HIGH)

            GPIO.output(22, GPIO.LOW)
            time.sleep(ingredient2)
            GPIO.output(22, GPIO.HIGH)

    # Define Pump Ingredient String
    default_string = "(Choose Your Poison)"
    pump_1_status = StringProperty(default_string)
    pump_2_status = StringProperty(default_string)
    pump_3_status = StringProperty(default_string)
    pump_4_status = StringProperty(default_string)
    pump_5_status = StringProperty(default_string)
    pump_6_status = StringProperty(default_string)
    # Change Pump Ingredient Based on Selection
    def change_text(self, pump, ingredient):
        if pump == "pump_1":
            self.pump_1_status = ingredient.capitalize()
        if pump == "pump_2":
            self.pump_2_status = ingredient.capitalize()
        if pump == "pump_3":
            self.pump_3_status = ingredient.capitalize()
        if pump == "pump_4":
            self.pump_4_status = ingredient.capitalize()
        if pump == "pump_5":
            self.pump_5_status = ingredient.capitalize()
        if pump == "pump_6":
            self.pump_6_status = ingredient.capitalize()

    # Set the Pump Ingredients
    def set_pump_one(wtf, pump, ingredient):
        # Open the Pump_config JSON
        with open("pump_config.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            # Set the Pump to change
            tmp = data[pump]
            # Update the `value`
            data[pump]["value"] = ingredient
            # Rewind cursor to beginning of file
            jsonFile.seek(0)
            json.dump(data, jsonFile)
            # Truncate incase new data is shorter than original data
            jsonFile.truncate()

class SmarTenderApp(App):
    def build(self):
        return Main()

if __name__ == "__main__":
	SmarTenderApp().run()
