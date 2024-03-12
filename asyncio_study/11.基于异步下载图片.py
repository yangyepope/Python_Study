import asyncio
import requests


async def download_image(url):
    print("开始下载图片", url)
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print("下载完成")
    fime_name = url.rsplit('/')[-1]
    with open(fime_name, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
    ]

    tasks = [download_image(url) for url in url_list]
    asyncio.run(asyncio.wait(tasks))
