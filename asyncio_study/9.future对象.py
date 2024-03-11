import asyncio


async def func():
    # 获取当前事件循环
    loop = asyncio.get_event_loop()

    # 创建一个任务(future对象),这个任务什么都不敢
    future = loop.create_future()

    # 等待任务最终结果(Future对象), 没有结果则会一直等下去
    await future


asyncio.run(func())
