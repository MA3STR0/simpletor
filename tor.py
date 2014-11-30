import socks
import socket


class Tor(object):
    """Tor class for socks proxy and controller"""
    def __init__(self, socks_port=9050):
        self.socks_port = socks_port
        self.default_socket = socket.socket
