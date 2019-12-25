from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Bartender():
    def __init__(self):
        GPIO.cleanup()
        # load the pump configuration from file
        self.pump_configuration = Bartender.readPumpConfiguration()
        for pump in self.pump_configuration.keys():
                GPIO.setup(self.pump_configuration[pump]["pin"], GPIO.OUT, initial=GPIO.HIGH)

        @staticmethod
        def readPumpConfiguration():
                return json.load(open('pump_config.json'))

class Main(TabbedPanel):
    def activate_pump(s):
        print "Turning motor on"
        GPIO.output(17,GPIO.HIGH)

class SmarTenderApp(App):
    def build(self):
        return Main()

if __name__ == "__main__":
	SmarTenderApp().run()
