# 练习函数式编程的map和reduce
from functools import reduce


l = [x for x in range(-10, 10, 2)]
print(l)
l = list(map(abs, l))
print(l)


# reduce是将列表做累计运算
# lambda是匿名函数
num = reduce(lambda x, y: x + y, l)
print(num)


# 将一个字符串转换成整型
def str2int(s):
    def char2int(ch):
        c = {str(x): x for x in range(10)}
        return c[ch]

    def fun(n1, n2):
        return n1*10 + n2

    return reduce(fun, map(char2int, s))


num = str2int('12345')
print(type(num), num)


# 这是使用匿名函数的简便版
def str2int2(s):
    ch = {str(x): x for x in range(10)}
    return reduce(lambda x, y: x*10+y, map(lambda x: ch[x], s))


num = str2int2('12345')
print(type(num), num)


# 作业：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    # capitalize()函数是将字符串的首字母大写
    return list(map(lambda x: x.capitalize(), name))


L = ['adam', 'LISA', 'barT']
print(normalize(L))


# 作业2：Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(x, y):
    return x*y


num = reduce(prod, [3, 5, 7, 9])
print(num)


# 作业3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    ch = {str(x): x for x in range(10)}
    # 先将字符串分割
    L = s.split('.')
    # 整数部分
    n1 = reduce(lambda x, y: x*10 + y, map(lambda x: ch[x], L[0]))
    # 小数部分
    n2 = reduce(lambda x, y: x * 10 + y, map(lambda x: ch[x], L[1]))
    n2 *= 0.1**len(L[1])
    return n1+n2


num = str2float('123.456')
print(num)
