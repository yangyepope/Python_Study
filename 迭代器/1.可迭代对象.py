"""
概念： 可以直接作用于for循环的对象统称可迭代对象（Iterable）

可以直接作用于for循环的数据类型：
   1. 集合数据类型， 如 list、tuple、dict、set、string
   2. generator， 包含生成器和带yield的generator function

   注意： 可以使用isinstance() 函数判断一个对象是否为Iterable对象
"""
from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance([], Iterable))
print(isinstance(100, Iterable))


