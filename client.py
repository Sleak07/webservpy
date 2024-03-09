
import socket

# defining the server and post of server side

HOST = "127.0.0.1" # server host IP
PORT = 65432 # port used by server

# Establishing the connection with server

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as so :
    so.connect((HOST,PORT))
    so.sendall(b"Hello from lvim python")
    data = so.recv(1024)

print(f"Recieved {data!r}")


