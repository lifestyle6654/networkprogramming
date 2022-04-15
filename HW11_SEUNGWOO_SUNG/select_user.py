from socket import *
import time, selectors

BUFF_SIZE = 1024

def device1(conn, mask):
    msg = conn.recv(BUFF_SIZE)
    
    temperature, humidity, light = msg.decode().split('/')

    current_time = time.strftime('%c', time.localtime(time.time()))
    
    f = open("data.txt", "a")
    f.write(current_time + ": Temp=" + temperature + ", Humid=" + humidity + ", lilum=" + light + '\n')
    f.close()

def device2(conn, mask):
    msg = conn.recv(BUFF_SIZE)

    heartbeat, steps, cal = msg.decode().split('/')

    current_time = time.strftime('%c', time.localtime(time.time()))

    f = open("data.txt", "a")
    f.write(current_time + ": Heartbeat=" + heartbeat + ", Steps=" + steps + ", Cal=" + cal + '\n')
    f.close()

# device1 소켓 생성
sock1 = socket(AF_INET, SOCK_STREAM)
sock1.connect(('localhost', 8888))

# devie2 소켓 생성
sock2 = socket(AF_INET, SOCK_STREAM)
sock2.connect(('localhost', 9999))

sock1.send(b'Register')
sock2.send(b'Register')

sel = selectors.DefaultSelector()
sel.register(sock1, selectors.EVENT_READ, device1)
sel.register(sock2, selectors.EVENT_READ, device2)

while True:
    # 등록된 객체에 대한 이벤트 감시 시작
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

    
