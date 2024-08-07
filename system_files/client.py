import socket 
import os

def upload_file(filepath):
     with open(filepath, 'rb') as f:
       while True:
        try:
            data = f.read(1024)
        except:
             print('the file has upload')
             break
        print('Sending data', data.decode())
        s.send(data)
        print('Sent data', data.decode())
        f.close()

def download_file(filepath):
    with open(filepath, 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:    
                break
            print('getting data', data.decode())
            f.write(data)
        print('the file has download')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080
s.connect(('127.0.0.1', port)) 
print (s.recv(1024))
choice = input()
s.sendall(choice.encode())
print (s.recv(1024))
fileName=input()
s.sendall(fileName.encode())
filepath = os.path.join('C:\\Users\\yonat\\OneDrive\\Desktop\\py\\pyc\\system_files', fileName)

if choice=="1":
    upload_file(filepath)
else:
    download_file(filepath)  
    
   

