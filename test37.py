#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习正则表达式'

__author__ = 'sergiojune'
import re


# 作业：尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email
a = 'someone@gmail.com'
b = 'bill.gates@microsoft.com'
# 匹配邮箱的正则表达式，返回一个正则对象
re_mail = re.compile('[\.\w]*@[\w]+.[\w]+')
m = re_mail.match(a)
print(m.group())
g = re_mail.match(b)
print(g.group())


# 版本二：
a = '<Tom Paris> tom@voyager.org => Tom Paris'
b = 'bob@example.com => bob'
mail = re.compile('([\w]+|[<>\w\s]+)@[\w]+.[\w]+')
aa = mail.match(a)
bb = mail.match(b)
print(aa.group())
print(bb.group())
