# 1초 후에 'hello', 2초 후에 'world'를 출력하는 프로그램
# 비동기 방식

import asyncio, time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

