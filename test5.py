# 练习列表生成式,这个很好用，越用越爽


l = [x for x in range(10)]
print(l)
# 还可以加条件来筛选元素,这里筛选偶数
l = [x for x in range(10) if x % 2 == 0]
print(l)
# 对两个列表生成一个也可以,生成全排列
l = [x + y for x in 'XYZ' for y in 'abc']
print(l)
# 也可以生成字典
d = {x:y for x in 'xyz' for y in 'ABC'}
print(d)


# 作业：将列表的字符串的大写改成小写，不是字符串的就去掉
L1 = ['Hello', 'World', 18, 'Apple', None]
print(L1)
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

