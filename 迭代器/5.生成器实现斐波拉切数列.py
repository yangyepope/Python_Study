#  生成器实现


def fib(count):
    index = 0
    x, y = 0, 1
    while index < count:
        yield y
        x, y = y, x + y
        index += 1


list = []

g = fib(100)
for i in g:
    print(i)
    list.append(i)

print(list)
