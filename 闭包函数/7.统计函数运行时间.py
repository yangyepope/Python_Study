import time


def wrapper(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
        # return end - start

    return inner


@wrapper
def timer():
    time.sleep(3)


timer()
# print(timer())
