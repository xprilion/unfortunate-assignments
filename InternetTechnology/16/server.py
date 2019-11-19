import socket
from datetime import date

host = '127.0.0.1'
port = 5000

s = socket.socket()

s.bind((host, port))
s.listen(1)

c, addr = s.accept()
print("Connection From: " + str(addr))

today = date.today()
today = str(today.strftime("%d/%m/%Y"))

print("Sending: " + today)
c.send(today.encode('utf-8'))

c.close()
