from socket import *
import threading, random
from time import sleep

BUFF_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9999))
s.listen(10)

conn, addr = s.accept()

msg = conn.recv(BUFF_SIZE)

if not msg:
    conn.close()
elif msg == b'Register':
    print('Message : ', addr, msg.decode())

while True:
    heartbeat = random.randrange(40, 140)
    steps = random.randrange(2000, 6000)
    cal = random.randrange(1000, 4000)

    conn.send(f'{heartbeat}/{steps}/{cal}'.encode())
    sleep(5)
