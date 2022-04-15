from socket import *

s = socket(AF_INET, SOCK_STREAM) # TCP 연결선언 SOCK_STREAM, UDP는 SOCK_DGRAM
s.bind(('', 9000)) # 서버 소켓을 특정 주소와 포트에 바인드 시킴
s.listen(2) # 바인딩 후, 서버는 클라이언트 연결을 기다림 listen(2) -> 동시에 2개의 연결가능

while True:
    client, addr, = s.accept() # 새로운 연결을 허용하기 위한 aceppt() 메소드 호출
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    client.close() # 클라이언트와의 연결 종료