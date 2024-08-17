from pynput.mouse import Button, Controller
import socket 
import ast

mouse = Controller()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5050
s.connect(('10.100.102.39', port))

while True:
    try:
        data=s.recv(1024).decode()
        data_tuple = ast.literal_eval(data)
        x, y = data_tuple[1]
        if data_tuple[0]=='1':   
            mouse.position = (x, y)
        elif data_tuple[0]=='2':
            mouse.click(Button.left)
        else:
            mouse.click(Button.right)
    except:
        break
        
