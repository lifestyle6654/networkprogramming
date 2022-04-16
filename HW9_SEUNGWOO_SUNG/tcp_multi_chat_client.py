# TCP를 이용한 단체 채팅 프로그램(멀티쓰레드): 클라이언트


from socket import *
import threading

def handler(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 4444))

my_id = input('ID를 입력하세요: ')
s.send(('[' + my_id + ']').encode())

th = threading.Thread(target=handler, args=(s,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + ']' + input()
    s.send(msg.encode())