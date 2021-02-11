from time import sleep_ms
from machine import Pin, PWM


class MicroLedController:
    def __init__(self, pin_red=12, pin_green=13, pin_blue=14, frequency=5000, duty=256):
        # led pins
        self.pin_red = pin_red
        self.pin_green = pin_green
        self.pin_blue = pin_blue
        # pwm leds
        self._led_pwm_red = None
        self._led_pwm_green = None
        self._led_pwm_blue = None
        # init LEDs
        self._led_init(self.pin_red, self.pin_green, self.pin_blue, frequency, duty)

    def _led_init(self, pin_red, pin_green, pin_blue, freq, duty):
        """
        Initializes all LEDs
        """
        self._led_pwm_red = PWM(Pin(pin_red, Pin.OUT), freq=freq, duty=duty)
        self._led_pwm_green = PWM(Pin(pin_green, Pin.OUT), freq=freq, duty=duty)
        self._led_pwm_blue = PWM(Pin(pin_blue, Pin.OUT), freq=freq, duty=duty)

    def _led_deinit(self):
        """
        De-initializes all LEDs
        """
        for led in [self._led_pwm_red, self._led_pwm_green, self._led_pwm_blue]:
            if led is not None:
                led.deinit()

    def __set_duty_all(self, duty):
        """
        Sets all the duty the same
        """
        self._led_pwm_red.duty(duty)
        self._led_pwm_green.duty(duty)
        self._led_pwm_blue.duty(duty)
        
    def set_rgb(self, red, green, blue):
        """
        Sets RBG LEDS individually
        """
        self._led_pwm_red.duty(red)
        self._led_pwm_green.duty(green)
        self._led_pwm_blue.duty(blue)

    def get_rgb(self):
        """
        Gets the RGB values of all LEDs
        """
        red = self._led_pwm_red.duty()
        green = self._led_pwm_green.duty()
        blue = self._led_pwm_blue.duty()
        return red, green, blue

    def pulse(self, sleep_duration_ms=5, repeat=1):
        """
        Gradually increases then decreases the duty cycle across all LEDs
        """
        for i in range(repeat):
            for duty_cycle in range(1024):
                self.__set_duty_all(duty_cycle)
                sleep_ms(sleep_duration_ms)
            for duty_cycle in range(1023, -1, -1):
                self.__set_duty_all(duty_cycle)
                sleep_ms(sleep_duration_ms)

    def start(self):
        """
        Runs a basic example
        """
        print('starting')
        self.pulse(repeat=10)

    def stop(self):
        self._led_deinit()
