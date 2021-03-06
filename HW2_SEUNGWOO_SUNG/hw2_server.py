import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    client.send(b'Hello ' + addr[0].encode())

    name = client.recv(1024)
    print(name.decode('utf-8'))

    student_number = 20171516 # 정수형 학번 생성
    # 정수를 네트워크 바이트 순서의 bytes 객체로 변경 후 전송
    student_number2 = student_number.to_bytes(4, 'big') 
    client.send(student_number2)

    client.close()