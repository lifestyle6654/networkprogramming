# ping 클라이언트
# ping 서버에 접속한 후, 1초 간격으로 10회 ping을 전송

import asyncio

async def ping_client():
    reader, writer = await asyncio.open_connection(host='localhost',port=8000)
    for _ in range(10):
        writer.write(b'ping')
        print('send: ping')
        
        data = await reader.read(8)
        print('recv:',data.decode())
        await asyncio.sleep(1)
    
    writer.write(b'done')
    print('send: ping')
    writer.close()
    await writer.wait_closed()
    print('connection was closed')
    
if __name__ == "__main__":
    asyncio.run(ping_client())