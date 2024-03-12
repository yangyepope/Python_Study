# count装饰器的参数
def wrapper(count):
    # func需要修饰的函数
    def decorator(func):
        # *args, **kwarg函数的参数
        def inner(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)

        return inner

    return decorator


@wrapper
def hello(name):
    print("hello %s" % name)


hello("Jack")
