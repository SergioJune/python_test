# 练习高级特性的迭代器
from collections import Iterable, Iterator

l = [1, 3, 5]
t = (1, 6, 5)
s = 'dsjk'
# 判断是否可迭代
print(isinstance(l, Iterable))
print(isinstance(t, Iterable))
print(isinstance(s, Iterable))
# 判断是否是迭代器,可以看出，这三个都不是迭代器
print(isinstance(l, Iterator))
print(isinstance(t, Iterator))
print(isinstance(s, Iterator))
# 判断生成器是否是迭代器,是的
print(isinstance((x for x in range(3)), Iterator))
# 同时也是可迭代的
print(isinstance((x for x in range(3)), Iterable))


# 我们可以将list，tuple，和string转成迭代器,这时就是迭代器了
print(isinstance(iter(l), Iterator))
print(isinstance(iter(t), Iterator))
print(isinstance(iter(s), Iterator))


# 其实for循环就是通过next来不断获取下一个元素的，直到抛出异常StopIteration
