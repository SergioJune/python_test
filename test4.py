# 练习高级特性的迭代


l = list(range(1,21))
# 这个就是迭代
for num in l:
    print(num)
# 对元组的迭代
t = (1,3,5,7,9)
for num in t:
    print(num)
# 还可以对字符串进行迭代
s = 'jskldf'
for c in s:
    print(c)


# 判断一变量是否可迭代，用collections的Iterable
from collections import Iterable
print(isinstance(l,Iterable))
print(isinstance(t,Iterable))
print(isinstance(s,Iterable))
# 可以看出结果都是True，证明可迭代


# 还可以按下表来迭代
for value,num in enumerate(t):
    print(value, num)


# 作业：请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def getNum(L):
    if isinstance(L,list):
        max = min = L[0]
        for num in L:
            if num > max:
                max = num
            if num < min:
                min = num
        return (min, max)
    else:
        print('请输入一个列表')


l = [9,5,456,8,54,4,45]
print(getNum(l))