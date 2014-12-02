import socks
import socket


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
        pass
