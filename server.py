import socket

s = socket.socket()
print('SOCKET CREATED')

s.bind(('localhost', 9999))

s.listen(3)
print("WAIT FOR THE CONNECTION")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()

    print('CONNECTED WITH', addr, name)

    c.send(bytes('WELCOME DUDE', 'utf-8'))

    c.close()
