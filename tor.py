import socks
import socket
import json
from stem.control import Controller
from stem import Signal
from urllib2 import urlopen


class Tor(object):
    """Tor class for socks proxy and controller"""
    def __init__(self, socks_port=9050, control_port=9051, control_password=""):
        self.socks_port = socks_port
        self.control_port = control_port
        self.control_password = control_password
        self.default_socket = socket.socket

    def connect(self):
        """connect to Tor socks proxy"""
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", self.socks_port)
        socket.socket = socks.socksocket

    def disconnect(self):
        """disconnect Tor socks proxy"""
        socket.socket = self.default_socket

    def change_relay(self):
        """change Tor relay to obtain new ip"""
        with Controller.from_port(port=self.control_port) as controller:
            controller.authenticate(self.control_password)
            controller.signal(Signal.NEWNYM)

    def print_ip():
        """print ip for debug"""
        json_str = urlopen('http://ip-api.com/json').read().decode('UTF-8')
        ip_dict = json.loads(json_str)
        for key, value in ip_dict.items():
            print("%s: %s" % (key, value))
