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
        c.sendall((x, y).encode())

    def on_click(x, y, button, pressed):
        c.sendall('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)).encode())
    
    def on_scroll(x, y, dy):
        c.sendall('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)).encode())

    with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
        listener.join()

    listener = mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll)
    listener.start()

    
    
#צריך 4 תיוגים, תיוג ראשון על סימון תזוזה, תיוג שני קליק שמאל, תייוג שלישי קליק ימין, תיוג רביעי גלגלת
    
    
    while True:
            try:
                print(c.recv(1024).decode())
            except:
                break