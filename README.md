# MicroLedStrip

A MicroPython app that allows a non-addressable LED strip to be controlled via WiFi.


## Uploading
If you're using the Adafruit MicroPython tool (ampy), you can use `upload.sh` to copy the files for you!
```commandline
pip3 install adafruit-ampy
./upload.sh
```

## Usage
```python
from micro_led_strip import MicroLedStrip

strip = MicroLedStrip(pin_red=12, pin_green=13, pin_blue=14)
strip.start()

```