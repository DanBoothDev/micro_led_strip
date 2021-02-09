from time import sleep
from machine import Pin, PWM


class MicroLedController:
    def __init__(self, pin_red=12, pin_green=13, pin_blue=14, frequency=1000, duty=512):
        # led pins
        self.pin_red = pin_red
        self.pin_green = pin_green
        self.pin_blue = pin_blue
        # pwm leds
        self._led_pwm_red = None
        self._led_pwm_green = None
        self._led_pwm_blue = None
        # init LEDs
        self._led_init(pin_red, pin_green, pin_blue, frequency, duty)

    def _led_init(self, pin_red, pin_green, pin_blue, frequency, duty):
        """
        Initialized all LEDs
        """
        self._led_pwm_red = PWM(Pin(pin_red, Pin.OUT), freq=frequency, duty=duty)
        self._led_pwm_green = PWM(Pin(pin_green, Pin.OUT), freq=frequency, duty=duty)
        self._led_pwm_blue = PWM(Pin(pin_blue, Pin.OUT), freq=frequency, duty=duty)

    def _led_deinit(self):
        """
        De-initialized all LEDs
        """
        for led in [self._led_pwm_red, self._led_pwm_green, self._led_pwm_blue]:
            if led is not None:
                led.deinit()

    def set_rgb(self, red, green, blue):
        """
        Sets RBG LEDS individually
        """
        self._led_pwm_red.duty(red)
        self._led_pwm_green.duty(green)
        self._led_pwm_blue.duty(blue)

    def start(self):
        """
        Runs a basic example
        """
        print('starting')
        for duty_cycle in range(0, 1024):
            self.set_rgb(duty_cycle, duty_cycle, duty_cycle)
            sleep(0.005)

    def stop(self):
        self._led_deinit()
