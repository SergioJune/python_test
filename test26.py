#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习错误处理'

__author__ = 'sergiojune'
import logging
from functools import reduce


def foo(n):
    # 自定义抛出错误
    if n == 0:
        raise ZeroDivisionError('被除数不能为零')
    return 10 / n


print(foo(20))
# 这个就会出错
# print(foo(0))


# 捕捉错误
try:
    n = input('请输入一个数字')
    n = int(n)
    res = 10 / n
    print(res)
# 有多种异常情况，所以有多个except语句块
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    # 用这个记录错误，开发中会发在日志上查看
    logging.exception(e)

# 当没有发生错误时会执行
else:
    print('成功运行')
# 这个语句块是必须执行的
finally:
    print('代码执行完毕')

print('end')


# 还可以自己创建异常
# 只需要继承自某一个异常就可以了，不过一般不需要自定义异常
class FooException(BaseException):
    pass


# 作业：运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        logging.exception(e)
        print('捕捉成功')
        try:
            return float(s)
        except ValueError as e:
            print(e)
            print('输入的内容不是数字')


def calc(exp):
    try:
        ss = exp.split('+')
        ns = map(str2num, ss)
        return reduce(lambda acc, x: acc + x, ns)
    except TypeError as e:
        print(e)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
print('end')
