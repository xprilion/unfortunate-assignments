import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()

s.bind((host, port))
s.listen(1)

c, addr = s.accept()
print("Connection From:" + str(addr))

data = c.recv(1024).decode('utf-8')

while(data != ":q"):
    print(str(addr) +" says: " + data)

    response = "Echo back - " + data
    c.send(response.encode('utf-8'))
    
    data = c.recv(1024).decode('utf-8')

c.close()
print(str(addr) + " closed connection.")