from socket import *
import random
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)

print('IoT server is running...')

while True:
    conn, addr = sock.accept()
    
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg != b'Request':
        print('client:', addr, msg.decode())
        conn.close()
        continue
    else:
        print('client:', addr, msg.decode())

    temperature = random.randrange(0, 40)
    humidity = random.randrange(0, 100)
    light = random.randrange(70, 150)
    num = 1
    num2 = num.to_bytes(4, 'big')

    conn.send(num2)
    conn.send(str(temperature).encode())
    conn.send(str(humidity).encode())
    conn.send(str(light).encode())

    msg = conn.recv(BUF_SIZE)
    
    if not msg:
        conn.close()
        continue
    elif msg != b'quit':
        print('client', addr, msg.decode())
        conn.close()
        continue
    else:
        print('Bye')

    conn.close()