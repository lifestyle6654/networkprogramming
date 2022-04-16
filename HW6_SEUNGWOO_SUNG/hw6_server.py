from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

global resp_data
resp_data = []
global resp_data2
resp_data2 = []
global resp_data3
resp_data3 = []

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    msg = data.decode()
    global req 
    req = msg.split(' ', maxsplit=2) # ['send', '1', 'Hello,', Iot']

    if msg == 'quit':
        resp = 'Bye'
        sock.sendto(resp.encode() ,addr)
        break

    if req[0] == 'send':
        if req[1] == '1':
            resp_data.append(req[2])
            # resp_data = str(req[2])
            print(resp_data)
            resp = 'Ok'
            sock.sendto(resp.encode(), addr)

        elif req[1] == '2':
            resp_data2.append(req[2])
            # resp_data2 = str(req[2])
            print(resp_data2)
            resp = 'Ok'
            sock.sendto(resp.encode(), addr)

        elif req[1] == '3':
            resp_data3.append(req[2])
            # resp_data3 = str(req[2])
            print(resp_data3)
            resp = 'Ok'
            sock.sendto(resp.encode(), addr)

        else:
            resp = 'No messages'
            sock.sendto(resp.encode(), addr)

    if req[0] == 'receive':
        if req[1] == '1':
            if len(resp_data) == 0:
                resp = 'No message'
                sock.sendto(resp.encode(), addr)
            else:
                sock.sendto(str(resp_data[0]).encode(), addr)
                del resp_data[0]
                

        elif req[1] == '2':
            if len(resp_data2) == 0:
                resp = 'No message'
                sock.sendto(resp.encode(), addr)
            else:
                sock.sendto(str(resp_data2[0]).encode(), addr)
                del resp_data2[0]
                

        elif req[1] == '3':
            if len(resp_data3) == 0:
                resp = 'No message'
                sock.sendto(resp.encode(), addr)
            else:
                sock.sendto(str(resp_data3[0]).encode(), addr)
                del resp_data3[0]
        
        else:
            resp = 'No message'
            sock.sendto(resp.encode(), addr)
                

sock.close()

