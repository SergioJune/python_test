#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习内建模块之contextlib'

__author__ = 'sergiojune'
import contextlib  # 这个模块是用来设置上下文管理器的，里面有两个很好用的装饰器
import requests

class Query():
    def __init__(self, name):
        self.name = name

    def query(self):
        print('query data is %s' % self.name)


@contextlib.contextmanager
# 这个方法不是类的
def create_query(name):
    q = Query(name)
    yield q  # 生成器，用with就是返回这个东西
    print('end')  # 当语句块执行完时就执行这个语句


with create_query('bob') as q:
    q.query()
    print('query end')


# 可以用上面的装饰器实现在运行代码之前自动运行某些代码
class Html(object):
    def __init__(self, name):
        self.name = name

    def put_start(self):
        print('<%s>' % self.name, end='')

    def put_end(self):
        print('</%s>' % self.name)


@contextlib.contextmanager
def create(name):
    h = Html(name)
    h.put_start()
    yield h
    h.put_end()


with create('h1') as h:
    print('我是标题', end='')


# 如果一个对象没有实现上下文方法，我们还可以用colsing这个方法
with contextlib.closing(requests.get('https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001478651770626de401ff1c0d94f379774cabd842222ff000')) as f:
    print(f.text)



