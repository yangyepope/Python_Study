import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('666')


async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    # await loop.create_task(set_after(future))
    await set_after(future)

    data = future
    print(data)


asyncio.run(main())
