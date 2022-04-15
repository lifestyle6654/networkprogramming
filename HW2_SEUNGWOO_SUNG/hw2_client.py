import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

# 문자열을 bytes 객체로 변환하여 전송
name = "Seungwoo Sung"
sock.send(name.encode('utf-8')) 

student_number = sock.recv(1024)
# 서버에서 받아온 bytes 객체의 학번을 정수형으로 변환하여 출력
student_number2 = int.from_bytes(student_number, 'big') 
print(student_number2)

sock.close()