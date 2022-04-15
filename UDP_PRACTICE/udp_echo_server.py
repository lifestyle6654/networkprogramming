from socket import *

port = 2500
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFF_SIZE)
    print('Received: ', msg.decode())

    sock.sendto(msg, addr)