#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习操作文件和目录'

__author__ = 'sergiojune'
import os
from datetime import datetime

# 获取操作系统的类型
print(os.name)
# window操作系统没有这个函数，在mac，linux下就会有
# print(os.uname())

# 环境变量
print(os.environ)
# 获取某个环境变量的值
print(os.environ.get('path'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))  # . 表示当前路径

# 添加目录
name = os.path.join(os.path.abspath('.'), 'testtest')  # 这步是解决不同系统目录名不一样的写法，是以目录形式合并两个参数
print(name)
# 用上面的结果来添加目录
# os.mkdir(name)
# 删除目录
# os.rmdir(name)

name = os.path.join(os.path.abspath('.'), 'test29.py')
print(name)
# 分割路径，会分出文件名和目录名
l = os.path.split(name)
print(l)
# 也可以直接分出文件名的后缀
t = os.path.splitext(name)
print(t)
# 重命名
# os.rename('test.txt', 'test.md')
# 删除文件
# os.remove('test.md')
# 找出目标路径是目录的名字
d = [x for x in os.listdir(r'E:\anaconda\python_project') if not os.path.isdir(x)]
print(d)


# 作业 1 ：利用os模块编写一个能实现dir -l输出的程序。
print('%s%30s' % ('type', 'name'))
for x in os.listdir(r'E:\anaconda\python_project'):
    # 判断是否是文件
    if os.path.isfile(x):
        file = os.path.splitext(x)[1]
        file = file.split('.')[1]
        print('%s%30s' % (file+' file', x))
    else:
        print('%s%30s' % ('folder', x))


# 作业2：编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
def find_dir(path, name, dirs=[]):
    for x in os.listdir(path):
        if os.path.isfile(path+'\\'+x):
            # 文件中有指定字符串
            if name in x:
                dirs.append(path+'\\'+x)
        # 文件夹
        else:
            if name in x:
                dirs.append(path+'\\'+x)
            # 递归
            find_dir(os.path.join(path, x), name)
    return dirs


d = find_dir(r'E:\anaconda\python_project', 'py')
print(d)

# 获取文件创建的时间
print(os.path.getmtime(d[0]))
print(datetime.fromtimestamp(os.path.getmtime(d[0])).strftime('%Y-%m-%d %H:%M:%S') )
# 获取文件大小
print(os.path.getsize(d[0])//1024, 'KB')

