#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习读取StingIO和BytesIO'

__author__ = 'sergiojune'
from io import StringIO, BytesIO

# StingIO和BytesIO 和在内存中读取数据，不是在文件中读取数据
s = StringIO('hello\nhi\ngood!\nheadsome boy')  # 创建
# 进行读取,与文件读取差不多
for x in s.readlines():
    print(x)
# 也可以这样创建
s = StringIO()
s.write('hello')
s.write(' ')
s.write('world')
print(s.getvalue())


# 这时BytesIO的练习,bytesIO是写入字节码，而SrtingIO是写入str
b = BytesIO('中文'.encode('utf-8'))
# print(b.getvalue())
print(b.read())
