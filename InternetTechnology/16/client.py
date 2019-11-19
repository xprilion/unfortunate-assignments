import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()

s.connect((host, port))

today = s.recv(1024).decode('utf-8')

print("Current Date Received From Server:" + today)

s.close()
