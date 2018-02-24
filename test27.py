#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习调试程序'

__author__ = 'sergiojune'
import logging
import pdb
# 这个标明打印信息的类别，不标明不会打印具体的错误信息
logging.basicConfig(level=logging.INFO)


def foo(n):
    # if n == 0:
    #     # 这个麻烦，可以用断言，这样没有输出
    #     print('n is zero !')
    # else:
    #     return 10 / n
    # 这个当条件为false时，就会执行后面语句，并抛出assertionError
    assert n != 0, 'n is zero !'
    return 10/n


foo(1)

s = '0'
n = int(s)
# 开发中用这个较多
logging.info('n = %d' % n)
print(10 / n)

# 还可以用pdb进行调试
s = '0'
n = int(s)
# 这个就是设置断点
pdb.set_trace()
logging.info('n = %d' % n)
print(10 / n)
