# import aiohttp
# import asyncio
#
#
# async def fetch(session, url):
#     print("请求发送", url)
#     async with session.get(url, verify_ssl=False) as response:
#         content = await response.content.read()
#         file_name = url.rsplit("_")[-1]
#         with open(file_name, "wb") as file_obj:
#             file_obj.write(content)
#             print('下载完成', url)
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         url_list = [
#             'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
#             'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
#             'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
#         ]
#         tasks = [
#             # 列表推导式
#             asyncio.create_task(fetch(session, url)) for url in url_list
#         ]
#         await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     # loop.close()
#     # asyncio.run(main())
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps

# !/usr/bin/env python
# -*- coding:utf-8 -*-
import aiohttp
import asyncio


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        print("1111")
        file_name = url.rsplit('_')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)
        print('下载完成', url)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
            'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
            'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]

        await asyncio.wait(tasks)


def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise

    return wrapper


if __name__ == '__main__':
    # asyncio.run( main() )
    _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)

    asyncio.run(main())
