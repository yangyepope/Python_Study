import time

import requests


def download_image(url):
    print("开始下载图片")
    res = requests.get(url)
    print("下载完成")
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_obj:
        file_obj.write(res.content)


if __name__ == '__main__':
    url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
    ]
    start_time = time.time()
    print(start_time)
    for url in url_list:
        download_image(url)
    end_time = time.time()
    print(end_time)


