# 여러 개의 코루틴 실행하기
# main() 코루틴 내에서, 코루틴으로 태스크를 생성 후 해당 태스크를 실행

import asyncio, time

async def add(a, b):
    print('In add() func')
    await asyncio.sleep(1)
    print(a + b)

async def mul(a, b):
    print('In mul() func')
    await asyncio.sleep(2)
    print(a * b)

async def main():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(add(1, 2))   # 코루틴으로 태스크 생성
    task2 = asyncio.create_task(mul(3, 4))   # 코루틴으로 태스크 생성
    await task1   # 태스크를 실행
    await task2   # 태스크를 실행
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())