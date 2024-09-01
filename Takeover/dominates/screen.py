import socket
import io
from PIL import Image
import time

s = socket.socket()
s.bind(('10.100.102.39',7070))
print(f'socket binded to port{7070}')
s.listen(1)
print('socket is listening')

c , addr = s.accept()
print ('got connection from', addr) 
while True:     
    bytes_len = c.recv(4)
    data_len = int.from_bytes(bytes_len, byteorder='big')
    
    img_data = b''
    while len(img_data) < data_len:
            packet = c.recv(4096)
            img_data += packet
    img = Image.open(io.BytesIO(img_data))
    img.show()
