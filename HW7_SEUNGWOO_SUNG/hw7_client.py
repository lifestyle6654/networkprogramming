from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

c_sock = socket(AF_INET, SOCK_DGRAM)

while True:
       
   msg = input('-> ')
   reTx = 0
   while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        c_sock.sendto(resp.encode(), ('localhost', port))
        c_sock.settimeout(2)

        try: 
           data, addr = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
           reTx += 1
           continue
        else:
           break

   c_sock.settimeout(None)
   while True:
      data, addr = c_sock.recvfrom(BUFF_SIZE)
      num = random.random()
      if num <= 0.5:
             continue
      else:
         c_sock.sendto(b'ack', ('localhost', port))
         print('<-', data.decode()) 
         break
