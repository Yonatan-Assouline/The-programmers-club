import socket
import threading
from pynput import keyboard 

def key_print():    
    while True:
        try:
            print(c.recv(1024).decode())
        except:
           break


def key_send(): 
    def key_press(key):
        c.sendall('{0} pressed'.format(key).encode())
    
    with keyboard.Listener(on_press=key_press) as listener:
       listener.join()

    listener = keyboard.Listener(on_press=key_press)
    listener.start() 


s = socket.socket()
s.bind(('127.0.0.1',8080))
print(f'socket binded to port{8080}')
s.listen(1)
print('socket is listening')


while True:
    c , addr = s.accept()
    print ('got connection from', addr) 
    

    thread1 = threading.Thread(target=key_send)
    thread2 = threading.Thread(target=key_print)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()