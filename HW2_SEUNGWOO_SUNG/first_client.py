import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

name = "Seungwoo Sung"
sock.send(name.encode('utf-8'))

student_number = sock.recv(1024)

student_number2 = int.from_bytes(student_number, 'big')
print(student_number2)

sock.close()