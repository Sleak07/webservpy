# building a simple tcp clent using python

import socket

# initalising the host and port constants

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as so:
    so.bind((HOST,PORT))
    so.listen()

    conn,addr = so.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data :
                break
            conn.sendall(data)
        
    



