from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    print(req)
    req2 = req[0].split(' ')
    print(req2)
    req3 = req2[1]
    print(req3)
    req4 = req3[1:] # index.html parsing
    print(req4)

    if req4 == 'index.html':
        f = open(req4, 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send('Content-Type: '.encode() + mimeType.encode() + '\r\n'.encode())
        c.send('\r\n'.encode())
        data = f.read()
        c.send(data.encode('euc-kr'))
    
    elif req4 == 'iot.png':
        f = open(req4, 'rb')
        mimeType = 'image/png'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send('Content-Type: '.encode() + mimeType.encode() + '\r\n'.encode())
        c.send('\r\n'.encode())
        data = f.read()
        c.send(data)

    elif req4 == 'favicon.ico':
        f = open(req4, 'rb')
        mimeType = 'image/x-icon'
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        c.send('Content-Type: '.encode() + mimeType.encode() + '\r\n'.encode())
        c.send('\r\n'.encode())
        data = f.read()
        c.send(data)
    else :
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send('<BODY>Not Found</BODY></HTML>'.encode())

    c.close()
