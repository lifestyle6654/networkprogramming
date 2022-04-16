from socket import *
import threading

port = 2500
BUFF_SIZE = 1204

# threading.Thread 클래스 상속받기
class ClientThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        # 소켓 초기화
        self.sock = sock
    
    def run(self):
        while True:
            data = self.sock.recv(BUFF_SIZE)
            if not data:
                break
            print('Received message:', data.decode())
            self.sock.send(data)

        self.sock.close()

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept()
    print('connected by', remotehost, remoteport)
    th = ClientThread(conn)
    th.start()