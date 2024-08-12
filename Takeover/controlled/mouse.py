from pynput import mouse
import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5050
s.connect(('10.100.102.39', port))

while True:
    try:
        data=s.recv(1024).decode()
    except:
        break
        