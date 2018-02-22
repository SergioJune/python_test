# 练习函数式编程的偏函数
import functools


print(int('12'))
print(int('12', 8))

# 偏函数，可以简单理解为将函数的某个参数固定住，从而简化调用函数的参数
# 与函数参数的默认参数类似
# 当函数参数比较多的时候可以选择使用偏函数

# 现在将int函数的禁止在位固定为8进制
# partial方法的第一个参数为函数名，第二个为固定的参数
int8 = functools.partial(int, base=8)
print(int8('12'))

kw = {'base': 2}
int2 = functools.partial(int, **kw)
print(int2('10'))


