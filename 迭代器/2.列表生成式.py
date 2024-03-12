"""

  Python内置的非常简单并且强大的可以用来生成list的生成式

"""

# 生成列表
# 缺点： 只能生成简单的列表


print(list(range(1, 11)))

li = []
for i in range(1, 11):
    li.append(i * i)

print(li)

# 列表生成式
li2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(li2)
