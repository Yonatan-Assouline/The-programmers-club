import socket
import os

def download_file(filepath):
    with open(filepath, 'wb') as f:
        while True:
            data = c.recv(1024)
            if not data:    
                break
            print('getting data', data.decode())
            f.write(data)
        print('the file has download')


def upload_file(filepath):
     with open(filepath, 'rb') as f:
       while True:
        try:
            data = f.read(1024)
        except:
             print('the file has upload')
             break
        print('Sending data', data.decode())
        c.send(data)
        print('Sent data', data.decode())
        f.close()


s = socket.socket()
print('socket is created')
s.bind(('127.0.0.1',8080))
print(f'socket binded to port{8080}')
s.listen(5)
print('socket is listening')


while True:
    c , addr = s.accept()
    print ('got connection from', addr)
    message = ('Welcome to my file storage system Type 1 if you want to upload files Type 2 if you want to download files')
    c.send(message.encode())
    data = c.recv(1024).decode()
    message = ('enter the file name')   
    c.send(message.encode())
    fileName = c.recv(1024).decode()
    filepath = os.path.join('C:\\Users\\yonat\\OneDrive\Desktop\\file_system', fileName)
    
    if data == '1':
        download_file(filepath)
    else:
        upload_file(filepath)    
    c.close()