from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 9999))
print("Time: ", sock.recv(1024).decode())
sock.close()
