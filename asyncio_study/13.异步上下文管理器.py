import asyncio


class AsyncContextManager:
    def __init__(self, conn):
        self.conn = conn

    async def do_some_thing(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步链接数据库
        self.conn = await asyncio.sleep(2)
        return self

    async def __aexit__(self):
        # 异步关闭数据库
        await asyncio.sleep(2)


async def func():
    async with AsyncContextManager('conn') as f:
        result = await f.do_something()
        print(result)


asyncio.run(func())
