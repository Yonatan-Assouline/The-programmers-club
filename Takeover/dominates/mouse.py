import socket
from pynput import mouse

s = socket.socket()
s.bind(('10.100.102.39',5050))
print(f'socket binded to port{5050}')
s.listen(1)
print('socket is listening')


while True:
    c , addr = s.accept()
    print ('got connection from', addr) 
    def on_move(x, y):
        cords = (x, y)
        data = ('1', cords)
        c.sendall(str(data).encode())

    def on_click(x, y, button, pressed):
        cords = (x, y)
        button_type = '2' if button == mouse.Button.left else '3'
        data = (button_type, cords)
        c.sendall(str(data).encode())
    
   
    with mouse.Listener(on_move=on_move,on_click=on_click) as listener:
        listener.join()

    listener = mouse.Listener(on_move=on_move,on_click=on_click,)
    listener.start()
