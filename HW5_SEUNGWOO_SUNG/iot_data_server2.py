from socket import *
import random
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
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

    heartbeat = random.randrange(40, 140)
    steps = random.randrange(2000, 6000)
    cal = random.randrange(1000, 4000)
    num = 2
    num2 = num.to_bytes(4, 'big')

    conn.send(num2)
    conn.send(str(heartbeat).encode())
    conn.send(str(steps).encode())
    conn.send(str(cal).encode())

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