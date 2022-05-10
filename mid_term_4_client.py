from socket import *
import random, time

port = 3333
BUFF_SIZE = 1024

c_sock = socket(AF_INET, SOCK_DGRAM)


while True:

    msg = 'ping'
    reTx = 0
    while reTx <= 2:
        c_sock.sendto(msg.encode(), ('localhost', port))
        send_time = time.time()
        c_sock.settimeout(1)

        try: 
            data, addr = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
           break
