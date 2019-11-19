import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()

s.bind((host, port))
s.listen(1)

c, addr = s.accept()
print("Connection From: " + str(addr))

data = c.recv(1024).decode('utf-8')
print("From Connected User: " + data)

data = data.upper()
print("Sending: " + data)
c.send(data.encode('utf-8'))

c.close()
