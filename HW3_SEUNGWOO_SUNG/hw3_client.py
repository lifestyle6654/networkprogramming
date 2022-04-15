from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Enter expression: ')

    if msg == 'q':
        break

    s.send(msg.encode())
    result = s.recv(1024).decode()

    print('Received message:', result)

s.close()