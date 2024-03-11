import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "pass"


async def main():
    print("main开始")
    task_list = [
        asyncio.create_task(func(), name='n1'),
        asyncio.create_task(func(), name='n2')
    ]
    print("main结束")

    done, pending = await asyncio.wait(task_list, timeout=None)
    print(done, pending)
    print(type(done))
    done = list(done)
    print(done)
    for i in done:
        print(i.result(), type(i))


if __name__ == '__main__':
    asyncio.run(main())
