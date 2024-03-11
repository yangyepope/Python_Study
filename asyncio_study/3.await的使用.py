import asyncio


async def func():
    response = await asyncio.sleep(2)
    print("等待结束")
    print("结束", response)


asyncio.run(func())
