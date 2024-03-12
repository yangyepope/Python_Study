import asyncio


class Reader(object):
    """自定义异步迭代器 （同时也是异步可迭代对象）"""

    def __init__(self):
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.readline()
        if value is None:
            raise StopAsyncIteration
        return value


async def func():
    obj = Reader()
    async for item in obj:
        print(item)


if __name__ == '__main__':
    asyncio.run(func())
