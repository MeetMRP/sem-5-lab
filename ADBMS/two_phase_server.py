# Server
import socket
host = "127.0.0.1"
port = 8000

s = socket.socket()
s.bind((host, port))
s.listen(3)
print("SERVER IS RUNNING")

msg = "PREPARE"
log = msg

over = 0

while True:
    replies = []
    print(f'Coordinator: {msg.upper()}')
    for i in range(3):
        c, addr = s.accept()
        c.send(msg.encode())
        data = c.recv(1024).decode()

        replies.append(data.upper())
        print(f'Subordinator: {data.upper()}')

    if 'ABORT' in replies:
        msg = 'ABORT'
        over = 1
        print(f"TRANSACTION LOG : {log} {msg}")
    elif 'SUCCESS' in replies:
        msg = 'COMPLETE'
        over = 1
        print(f"TRANSACTION LOG : {log} {msg}")
    else:
        msg = 'COMMIT'
        log += f' {msg}'