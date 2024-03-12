"""
 1. 参数、结果的检查
 2. 缓存 （缓存到redis中）

 3. 计数

 4. 日志

 5. 统计

 6. 权限管理

 7. 重试

"""


# 统计函数执行次数

def wrapper(f):
    index = 0

    def inner(*args, **kwargs):
        nonlocal index
        index += 1
        f(*args, **kwargs)
        print("第%d次执行" % index)

    return inner


@wrapper
def run():
    print("执行次数")


@wrapper
def run1():
    print("执行次数")


run()
run1()
run()
run1()
run()
