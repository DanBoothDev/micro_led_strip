import json
from micro_led_controller import MicroLedController
from micro_wifi.web_server import WebServer


class MicroLedStrip:
    def __init__(self, pin_red=12, pin_green=13, pin_blue=14):
        self.web_server = WebServer()
        # setup web server routes
        self.setup_routes(self.web_server)
        # setup led manager
        self.led_manager = MicroLedController(pin_red, pin_green, pin_blue)

    def start(self):
        # start our web server to allow the user to configure the device
        self.web_server.start()
        # start the led demo
        self.led_manager.start()

    def stop(self):
        try:
            self.web_server.stop()
            self.led_manager.stop()
        except Exception as exc:
            print('Error stopping {}'.format(exc))

    def setup_routes(self, server):
        @server.route("/")
        def home(client, request):
            html = ""
            try:
                with open('www/index.html') as f:
                    html = f.read()
            except OSError:
                pass
            server.send_response(client, html)

        @server.route("/update", 'POST')
        def connect(client, request):
            params = server.get_form_data(request)
            colour = params.get('colour')  # retrieve a seven-character hexadecimal notation
            print('colour {}'.format(colour))
            [red, green, blue] = self._rgb_str_to_led_pwm(colour[1:])
            self.led_manager.set_rgb(red, green, blue)
            payload = {
                'status': True,
                'msg': 'Successfully set colour {}'.format(colour)
            }
            server.send_response(client, json.dumps(payload), content_type='application/json')

    def _rgb_str_to_led_pwm(self, rgb_hex_str):
        """
        Converts a six-character hexadecimal string into an int array
        :param rgb_hex_str: string to convert. e.g. ff0033
        :return: colour array of [0-1023, 0-1023, 0-1023]
        """
        colours = []
        for index in range(0, len(rgb_hex_str), 2):
            hex_colour = rgb_hex_str[index: index + 2]
            # convert to int
            int_colour = int(str(hex_colour), 16)
            # double the val to boost the value
            colours.append(int_colour * 2)
        return colours
