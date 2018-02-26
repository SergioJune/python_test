#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习内建模块之collections'

__author__ = 'sergiojune'
from collections import namedtuple, defaultdict, deque, OrderedDict, Counter

# 弄一个可以根据名字来取数的元组
at = namedtuple('Point', ['x', 'y'])  # 第一个参数为描述事物类型， 第二个参数为元组的位置名字
p = at(1, 2)  # 新建一个元组
# 根据名字来取元素
print(p.x)  # 这就可以看作是一个坐标点
print(p.y)

# 有默认值的dict
dd = defaultdict(lambda:'not')  # 参数为遇到不存在键时的处理的方法
dd['age'] = 20
print(dd['age'])  # 存在
print(dd['a'])  # 不存在


# 使用队列，比list的插入数据和删除数据快，支持从头或者尾删除或插入
d = deque([1, 2, 3, 6])
print(d)
# 从头插入数据
d.appendleft(5)
print(d)
# 删除头部数据
d.popleft()
print(d)

# 让字典保持有序
od = OrderedDict([('x', 3), ('y', 6), ('z', 6)])
print(od)
# 还可以添加，与dict用法一样
ood = OrderedDict()
ood['f'] = 5
ood['s'] = 9
ood['e'] = 7
print(ood)


# 用计数器，直接算出某一个字符串里面字符出现的个数
s = 'mynameissergiojune'
c = Counter(s)
print(c)


# 利用OrderedDict实现一个先进先出的字典，超过最大容量的时候就删除
class LastUpdateDict(OrderedDict):
    def __init__(self, max):
        super(LastUpdateDict, self).__init__()
        self.max = max

    def __setitem__(self, key, value):
        # 看看有没有重复键
        contains = 1 if key in self.keys() else 0
        # 判断最大长度
        if len(self) - contains >= self.max:
            last = self.popitem(last=False)  # last 为false时就删除第一个添加的键值对，否则删除最后的键值对
            print('pop', last)
        # 增加元素
        if contains: # 键原来存在，直接修改
            del self[key]
            print('update', key, value)
        else:
            print('add', key, value)
        OrderedDict.__setitem__(self, key, value)


lud = LastUpdateDict(3)
lud['a'] = 1
lud['b'] = 2
lud['c'] = 3
print(lud)
lud['d'] = 4
print(lud)
lud['b'] = 5
print(lud)
