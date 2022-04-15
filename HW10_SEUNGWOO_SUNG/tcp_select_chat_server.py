import socket, select, time

socks = [] # 소켓 리스트
BUFFER = 1024  
PORT = 4444

s_sock = socket.socket() # TCP 소켓
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock) # 소켓 리스트에 서버 소켓을 추가
print('Server Started')

while True:
    # 읽기 이벤트(연결요청 및 데이터수신) 대기
    # 메시지 수신(읽기)만 체크할 것이기 때문에, 쓰기와 예외는 비워둠
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    # 수신(읽기 가능한) 소켓 리스트 검사
    for s in r_sock: 
        # 새로운 클라이언트의 연결 요청 이벤트 발생
        # 서버소켓이라면, (새로운 클라이언트의 연결 요청이 있다는 뜻)
        if s == s_sock:
            conn, addr = s_sock.accept()
            # 소켓 리스트에 새로운 클라이언트 추가
            socks.append(conn)
            print(f'Client ({addr} connected.')
        # 기존 클라이언트의 데이터 수신 이벤트 발생
        else:
            data = s.recv(BUFFER)
            msg = data.decode()
            if 'quit' in msg:
                print(addr, 'exited')
                s.close()
                socks.remove(s)
                continue

            print(time.asctime() + str(addr) + ':' + data.decode())
            
            for client in socks:
                if client != s and client != s_sock:
                    client.send(data)