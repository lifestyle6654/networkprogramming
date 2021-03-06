# 여러 개의 코루틴을 실행하기
# main() 코루틴 내에서 2개의 코루틴을 직접 실행

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
    await add(1, 2)    # 코루틴 1
    await mul(3, 4)    # 코루틴 2 
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())