def wrapper1(f):
    print("enter wrapper1")

    def inner1(*args, **kwargs):
        print("enter inner1")
        res = f(*args, **kwargs)
        print("exit inner1")
        return res

    print("exit wrapper1")
    return inner1


def wrapper2(f):
    print("enter wrapper2")

    def inner2(*args, **kwargs):
        print("enter inner2")
        res = f(*args, **kwargs)
        print("exit inner2")
        return res

    print("exit wrapper2")
    return inner2


"""
   装饰时，从距离近的装饰器开始装饰
   装饰过程如下：
        inner2 = wrapper2(func)
        inner1 = wrapper1(inner2)
        func = inner1
        
    执行过程如下：  从距离远的装饰器内部函数开始执行
    inner1
        
"""


@wrapper1
@wrapper2
def run():
    print("enter run")


print("++++++++++++++++++++++++++++++++")

run()

# enter wrapper2
# exit wrapper2
# enter wrapper1
# exit wrapper1
# enter inner1
# enter inner2
# enter run
# exit inner2
# exit inner1
