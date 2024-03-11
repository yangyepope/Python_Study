import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    print("main开始")

    # 创建Task任务，将当前执行func函数任务添加到事件循环
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    # ret1 = await task1
    ret1 = task1
    # ret2 = await task2
    ret2 = task2
    # print(ret1, ret2)


asyncio.run(main())
