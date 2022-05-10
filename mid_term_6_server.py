from socket import *
import random

port = 7777
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(10)


while True:
    conn, addr = sock.accept()

    msg = conn.recv(BUFF_SIZE)
    r_msg = str(msg.decode())

    if r_msg == '1':
        temp = random.randint(1, 50)
        temperature = temp.to_bytes(4, 'big')
        humid = (0).to_bytes(4,'big')
        lumi = (0).to_bytes(4, 'big')
        conn.send(temperature)
        conn.send(humid)
        conn.send(lumi)

    if r_msg == '2':
        hum = random.randint(1, 100)
        humid = hum.to_bytes(4, 'big')
        temperature = (0).to_bytes(4, 'big')
        lumi = (0).to_bytes(4, 'big')
        conn.send(temperature)
        conn.send(humid)
        conn.send(lumi)

    if r_msg == '3':
        lum = random.randint(1, 150)
        lumi = lum.to_bytes(4, 'big')
        temperature = (0).to_bytes(4, 'big')
        humid = (0).to_bytes(4, 'big')
        conn.send(temperature)
        conn.send(humid)
        conn.send(lumi)


