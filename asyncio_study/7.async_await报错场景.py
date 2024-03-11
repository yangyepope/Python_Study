import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


task_list = [
    # create_task会将任务马上加到事件循环上
    asyncio.create_task(func(), name='n1'),
    asyncio.create_task(func(), name='n2')
]


# 代码报错，此时task没有被加到事件循环中
done, pending = asyncio.run(asyncio.wait(task_list))
