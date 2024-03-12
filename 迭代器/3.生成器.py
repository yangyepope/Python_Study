"""
  生成器概念：  通过列表生成式，可以直接创建一个列表。所有的数据都会存到内存中，受内存的限制

"""

# 创建生成器

# 1、 修改列表生成式： 将列表生成式的[] 修改为()即可

g = (x * x for x in range(10))
print(g)
print(type(g))

# 生成器特点:  可以通过next()函数通过generator的下一个值,节省内存

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
    print(i)
