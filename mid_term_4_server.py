from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))


while True:
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE) 

        if random.randint(1, 10) <= 5:
            continue
        elif data.decode() != 'data':
            continue
        else:
            sock.sendto('pong'.encode(), addr)
            break