from socket import *
import threading

port = 3333
BUFF_SIZE = 1024

# 메시지를 송신하는 부분을 쓰레드로 구현
def sendTask(sock):
    while True:
        resp = input()
        # 입력받은 메시지를 화면에 출력
        print('->', resp)
        # 입력받은 메시지를 client로 송신
        sock.send(resp.encode())

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(1)
# 메인 쓰레드를 위한 소켓 설정
conn, addr = s.accept()

# 메시지를 송신하는 쓰레드 생성
th = threading.Thread(target=sendTask, args=(conn,))
th.start()

# 메인 쓰레드는 client로부터 메시지를 수신하여 출력하는 역할만 수행
while True:
    data = conn.recv(BUFF_SIZE)
    print('<-', data.decode())