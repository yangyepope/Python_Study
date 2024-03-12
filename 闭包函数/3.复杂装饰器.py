def wrapper(f):
    def inner(name, age):
        if age < 0:
            age = 0
        return f(name, age)

    return inner


@wrapper
def say(name, age):
    print("%s is %d years old" % (name, age))


say("Jack", -10)
