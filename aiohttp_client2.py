import aiohttp
import asyncio

async def main():
    async with aiohttp.request('GET', 'http://python.org/') as rsp:
        print(rsp.status)
        print(rsp.headers)
        print(await rsp.text())

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())