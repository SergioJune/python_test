#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习内建模块之base64'

__author__ = 'sergiojune'
import base64

# 进行base64编码，转为字符串
b = b'binary\x00strg='
bs = base64.b64encode(b)
print(bs)
# 解码
b = base64.b64decode(bs)
print(b)


# 对于网页的安全编码
s = b'i\xb7\x1d\xfb\xef\xff'
bs = base64.b64encode(s)
print(bs)
bs = base64.urlsafe_b64encode(s)
print(bs)


# 作业：请写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    while len(s) % 4 !=0:
        s += b'='
    bs = base64.b64decode(s)
    return bs


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')