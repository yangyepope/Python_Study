import time


def retry(count=3, wait=0, exception=(Exception,)):
    def decorator(func):
        def inner(*args, **kwargs):
            for i in range(count):
                try:
                    res = func(*args, **kwargs)
                except exception as e:
                    time.sleep(wait)
                    continue

                else:
                    return res

        return inner

    return decorator


import random


@retry(count=5, wait=3, exception=Exception)
def connectSQL():
    num = random.choice([1, 2, 3, 4])
    print("====================", num)
    if num <= 4:
        10 / 0


connectSQL()
