from socket import *
import time
import sys

BUF_SIZE = 1024
LENGTH = 4

s = socket(AF_INET, SOCK_STREAM)

s_num = input('1 or 2: ')
s_num2 = str(s_num)

if s_num2 == '1':
    s.connect(('localhost', 7777))
    s.send(b'Request')

if s_num2 == '2':
    s.connect(('localhost', 8888))
    s.send(b'Request')

num = s.recv(BUF_SIZE)
num2 = int.from_bytes(num, 'big')

msg = s.recv(BUF_SIZE)
msg2 = s.recv(BUF_SIZE)
msg3 = s.recv(BUF_SIZE)

if num2 == 1:
    f = open("data.txt", 'a')
    f.write(time.strftime('%c', time.localtime(time.time())) + ': ' + 'Temp=' +  msg.decode() + ', Humid=' + msg2.decode() + ', lilum=' + msg3.decode() + '\n')
    f.close()

if num2 == 2:
    f = open("data.txt", 'a')
    f.write(time.strftime('%c', time.localtime(time.time())) + ': ' + 'Heartbeat=' +  msg.decode() + ', Steps=' + msg2.decode() + ', Cal=' + msg3.decode() + '\n')
    f.close()

close_ment = input('if you want to finish, input quit still want data input con: ')
if close_ment == 'quit':
    s.send(close_ment.encode())
    s.close()

