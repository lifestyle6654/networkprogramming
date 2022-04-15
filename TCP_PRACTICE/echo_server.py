from socket import *
port = 2500
BUFF_SIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

conn, (remotehost, remoteport) = sock.accept()
print('connected by: ', remotehost, remoteport)

while True:
    data = conn.recv(BUFF_SIZE)
    if not data: # 예외 처리
        break
    print('Received message: ', data.decode())
    conn.send(data)

conn.close()
sock.close()