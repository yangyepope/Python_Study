"""
  装饰器的概念： 装饰器实际是一个闭包，把一个函数作为参数然后返回一个替代版函数，本质上就是一个返回函数的函数

"""


def func():
    print("Tom is a good man")


def wrapper(f):
    def inner(*args, **kwargs):
        print('-----------------------')
        f()

    return inner


wrapper(func)()
