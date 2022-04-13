from socket import *
import time
import threading

clients = []
port = 2500

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

while True:
    conn, addr = s.accept()

    if conn not in clients:
        print('new client', addr)
        clients.append(conn)

    th = threading.Thread(target=handle_receive, args=(conn, addr,))
    th.start()

s.close()
            

