import asyncio


async def others():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return '返回值'


async def func():
    print("执行协程函数代码")
    response = await others()
    print("IO请求结束，结果为:", response)


asyncio.run(func())
