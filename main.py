from micro_led_strip import MicroLedStrip
from micro_wifi.micro_wifi import MicroWifi

wifi = MicroWifi()
led_strip = MicroLedStrip()
# auto connect to network
wifi.start()
# start the led controller demo
led_strip.start()
