"""
   概念：  在函数体中定义内部函数，并且使用了外部函数的变量，然后把内部函数返回，那么这个内部函数就是闭包

   优点： 避免污染全局环境，这样就可以在函数体外使用函数体中定义的变量


   缺点： 数据长期驻留在内存中，造成内存极大的浪费
"""

a = 10


def func():
    b = 20

    def func2():
        # nonlocal b
        b = 40
        c = 30
        return b

    return func2  # 返回的是函数，而不是函数的返回值


f = func()
print(f())
