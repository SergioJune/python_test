#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习读取文件'

__author__ = 'sergiojune'


# 默认编码方式是gbk，而编译器是utf-8，所以需要指定编码方式
f = open('./test27.py', 'r', encoding='utf-8')
# 读取文件全部内容，有一个参数为读取文件的大小
# 当文件较小时可以这样读
# txt = f. read()
# print(txt)

# 还可以这样一行一行读
print(f.readline())
# 以一行行形式读全部内容
for line in f.readlines():
    print(line)
# 最后记得关闭文件
f.close()


# 当文件出现异常时，或许关闭不了文件，就需要捕捉异常
try:
    f = open('./test26.py', 'r', encoding='utf-8')
    for x in f.readlines():
        print(x)
except IOError as e:
    print(e)
finally:
    # 最后一定关闭
    if f:
        f.close()


# 如果每次都需要这样捕捉异常，就会很麻烦，python中可以用with语句块来处理
with open('./test27.py', 'r', encoding='utf-8') as f:
    # 当离开这个语句块就会自动关闭，就不需要我们来关闭
    txt = f.read()
    print(txt)


# 作业：请将本地一个文本文件读为一个str并打印出来
# 上面的就是了，参考上面的
