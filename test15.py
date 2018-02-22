#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'sergiojune'


# 上面是一个模块的正确写法
# 第一个注释是可以将这个代码直接运行在Unix/Linux/Mac上
# 第二行代码是说这个代码是以utf-8编写的
#  第三代码就是模块的文档注释
# 第四行代码就是作者标明

import sys
# 添加自己模块的查找位置，这样的方法当运行完就失效，可以想一直有用可以添加环境变量
sys.path.append(r'E:\anaconda\python_project')
# 导入自己的模块
import spider_ip
