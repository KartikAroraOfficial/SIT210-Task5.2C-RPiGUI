# This Python file uses the following encoding: utf-8
from gpiozero import LED
import RPi.GPIO as GPIO

red = LED(14)
green = LED(15)
blue = LED(18)


class led_controller(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def red(self):
        self.reset()
        red.on()

    def green(self):
        self.reset()
        green.on()

    def blue(self):
        self.reset()
        blue.on()

    def reset(self):
        red.off()
        green.off()
        blue.off()

    def controller_exit(self):
        GPIO.cleanup()

