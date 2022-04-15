from socket import *
import threading, random
from time import sleep

BUFF_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(10)

conn, addr = s.accept()

msg = conn.recv(BUFF_SIZE)

if not msg:
    conn.close()
elif msg == b'Register':
    print('Message : ', addr, msg.decode())

while True:
    temperature = random.randint(0, 40)
    humidity = random.randint(0, 100)
    light = random.randint(70, 150)

    conn.send(f'{temperature}/{humidity}/{light}'.encode())
    sleep(3)
