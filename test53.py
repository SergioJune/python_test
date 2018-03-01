#!/usr.bin.env python 3
# -*- coding: utf-8 -*-

'''
练习python的协程0
next(方法和next()方法在一定意义上是相同用法的，只不过next不能传递特定的值而next可以传递特定的值
next() 和send(None) 方法是等价的，都是用于启动生成器返回值
'''

__author__ = 'sergiojune'


# 消费者
def consumer():
    r = ''
    while True:
        n = yield r  # 接受调用者发送的数据
        if not n:
            return
        print('consumer consume is %s' % n)
        r = '200 OK'


def producer(c):  # 这个函数先被执行
    c.send(None)  # 这个语句必须写，而且参数固定，作用是启动上面的生成器
    x = 0
    while x < 5:
        x = x+1
        print('producer is produce %d' % x)
        r = c.send(x)  # 发送数据，生成器接受数据，赋值给n变量
        print('consumer is return %s' % r)
    # 关闭
    c.close()


c = consumer()
producer(c)
