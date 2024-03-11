import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "123"


task_list = [
    func(),
    func()
]

asyncio.run(asyncio.wait(task_list))
