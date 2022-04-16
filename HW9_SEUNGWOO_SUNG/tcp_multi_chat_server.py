# TCP를 이용한 단체 채팅 프로그램(멀티쓰레드): 서버

from socket import *
import time
import threading

clients = []
port = 2500

# UDP와 다르게 새로운 클라이언트를 받는 쓰레드를 따로 구현

# client로부터 받은 메시지를 출력하고 다른 클라이언트들에게 전송하는 쓰레드 구현
def handle_receive(conn, addr):
    while True:
        data = conn.recv(1024)
        msg = data.decode()
    # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
        if 'quit' in msg:
            if conn in clients:
                print(addr, 'exited')
                clients.remove(conn)
                continue

        else:
            print(time.asctime() + str(addr) + ':' + data.decode())

    # 모든 클라이언트에게 전송
            for client in clients:
                if client != conn:
                    client.send(data)

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

print('Server Start')

# 메인 쓰레드에서는 새로 들어온 client를 client 배열에 저장하는 역할을 수행
while True:
    conn, addr = s.accept()

    if conn not in clients:
        print('new client', addr)
        clients.append(conn)

    th = threading.Thread(target=handle_receive, args=(conn, addr,))
    th.start()

s.close()
            

