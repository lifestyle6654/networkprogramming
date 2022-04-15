from socket import *

s = socket(AF_INET, SOCK_STREAM) # TCP 소켓 선언 
s.connect(('localhost', 9000)) # 서버 주소로 접속
msg = s.recv(1024)
print(msg.decode())
s.close()

