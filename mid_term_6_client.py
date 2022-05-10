from socket import *

BUFF_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 7777)
s.connect(addr)

while True:
        msg = input('Input number -> ')
        s.send(msg.encode())

        r_msg = s.recv(BUFF_SIZE)
        r_msg2 = s.recv(BUFF_SIZE)
        r_msg3 = s.recv(BUFF_SIZE)

        r_msg = int.from_bytes(r_msg, 'big')
        r_msg2 = int.from_bytes(r_msg2, 'big')
        r_msg3 = int.from_bytes(r_msg3, 'big')


        print('Temp=' + str(r_msg) + ', Humid=' + str(r_msg2) + ', Lumi=' + str(r_msg3))
        break