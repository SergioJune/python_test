#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习内建模块之itertools'

__author__ = 'sergiojune'
import itertools  # 操作可迭代对象的

# # 无限迭代列表,这是个自然数列表，参数为起始数字,第二个参数为步长
# c = itertools.count(1)
# for x in c:
#     print(x)

# 无限循环迭代一个列表
# for x in itertools.cycle('abc'):
#     print(x)

# 重复迭代元素n次
# for x in itertools.repeat('abc', 6):  # 第二个参数为迭代次数
#     print(x)

# 用takewhile()方法停止无限循环的迭代
c = itertools.count(1,2)
l = list(itertools.takewhile(lambda x: x<10, c))  # 第一个为接受函数，返回False就停止迭代，第二个为无限迭代的列表
print(l)

# 把一组可迭代的对象连接起来
l1 = [x for x in range(5)]
l2 = {1, 3, 5}  # 不同类型也可以 连接起来
i = list(itertools.chain(l1, l2))
print(i)

# 将相同的元素分到同一组
for x, y in itertools.groupby('aaabbbccc'):
    print(x, list(y))

# 可以设置不区分大小写
for x in itertools.groupby('AABBCCaAcdb',lambda x: x.lower()):
    print(list(x)[0], list(list(x)[1]))


# 作业：计算圆周率可以根据公式：利用Python提供的itertools模块，我们来计算这个序列的前N项和
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_list = (x for x in itertools.count(1,2))
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    n_list = [next(odd_list) for x in range(N)]
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    calc_list = list(map(lambda x: (4/x) if (x-1)/2 % 2 == 0 else (-4/x), n_list))
    # step 4: 求和:
    s = sum(calc_list)
    return s


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
