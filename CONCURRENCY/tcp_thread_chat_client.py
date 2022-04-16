from socket import *
import threading

port = 3333
BUFF_SIZE = 1024

# 메시지를 수신하는 부분을 별도 쓰레드로 구현
def recvTask(sock):
    while True:
        data = sock.recv(BUFF_SIZE)
        print('<-', data.decode())

# 메인 쓰레드를 위한 소켓 생성
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', port))

# 메시지 수신하는 쓰레드 생성
th = threading.Thread(target=recvTask, args=(sock,))
th.start()

# 메인 쓰레드는 메시지를 입력받아 server로 송신하는 역할만 수행
while True:
    msg = input()
    print('->', msg)
    sock.send(msg.encode())