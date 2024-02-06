#TODO :  build a tcp server in python

from http import server
import socket
import threading

# defining the host

host = '127.0.0.1'
port = 55555

# starting server
server = socket.socket(socket.AF_INET)