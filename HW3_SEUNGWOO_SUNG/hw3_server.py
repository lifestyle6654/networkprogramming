from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            result = eval(data)
        except:
            client.send(b'Try again')
        else:
            client.send(str(result).encode())

    client.close()