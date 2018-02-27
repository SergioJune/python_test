#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习第三方模块之chardet'

__author__ = 'sergiojune'
import chardet  # 这个库是用来猜测字节码的编码方式的

s = b'hello world'
c = chardet.detect(s)
print(c)
# 结果：{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}，可以看出是ascii编码，第二个为概率，1.0表示百分百

s = '中国中文我爱你'
c = chardet.detect(s.encode('gbk'))
print(c)

c = chardet.detect(s.encode('utf-8'))
print(c)

# 看看日语的
s = '最新の主要ニュース'
c = chardet.detect(s.encode('euc-jp'))
print(c)

# encode()为编码，将字符串变为字节码，decode()为解码，将字节码转为字符串
