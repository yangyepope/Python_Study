def wrapper(f):
    def inner(*args, **kwargs):
        res = f(*args, **kwargs)
        return res

    return inner


@wrapper
def func(name):
    print('%s is good man' % name)
    return 'hello'


func("Jack")
