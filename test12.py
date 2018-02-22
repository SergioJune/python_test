# 练习函数式编程的匿名函数
from functools import reduce


# 用reduce来求一个列表的和
l = [x for x in range(11)]
# lambda的就是匿名函数，冒号前的表示参数，冒号后的表达式的结果为返回值
sum = reduce(lambda x, y: x + y, l)
print(sum)

# 还可以将匿名函数赋值给变量
f = lambda x: x * x
print(f(5))
print(f(8))


# 作业：改造代码
L = list(filter(lambda x: x % 2 == 1,range(1,20)))
print(L)
