"""
   推导的算法比较复杂，用列表生成式for循环无法实现的时候可以选择使用函数生成

"""


# 函数按顺序执行，遇到return语句或者最后一行函数语句就返回


# 如果想让一个函数变成生成器函数，只需要将函数的return改为yield
# generator函数，在使用调用next()的时候，遇到yield语句返回，如果再次执行next(),会从上次返回的yield语句处继续执行
def func():
    print("Tom is a good man")
    print("Tom is a nice man")
    print("Tom is a cool man")
    yield 10
    yield 20


# func()
print(func())
print(type(func()))
res = func()
print(next(res))
