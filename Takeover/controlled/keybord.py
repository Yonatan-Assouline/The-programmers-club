from pynput.keyboard import Key,Controller
import socket 
from pynput import keyboard as key1
import threading

def key_control():
    while True:
        try:
            key = s.recv(1024).decode()[1:2]
        except:
            break    
        if  len(key) == 1:
                keyboard.press(key)
        else:  
            special_key = getattr(Key, key, None)
            keyboard.press(special_key)

def key_send(): 
    while True:
        def key_press(key):
            s.sendall('{0} pressed'.format(key).encode())
    
        with key1.Listener(on_press=key_press) as listener:
            listener.join() 

        listener = key1.Listener(on_press=key_press)
        listener.start() 


keyboard = Controller()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080
s.connect(('127.0.0.1', port))



thread1 = threading.Thread(target=key_send)
thread2 = threading.Thread(target=key_control)

thread1.start()
thread2.start()

thread1.join()
thread2.join()