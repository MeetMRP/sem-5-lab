import socket

s = socket.socket()
print('socket created')

s.bind(('localhost', 9999))
s.listen(1)
print("server listning")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with ',addr, name)
    c.send(b'connected with 9999')
    c.close()