import asyncio


async def a(x):
    b = x * 2
    return b

asyncio.run(a)