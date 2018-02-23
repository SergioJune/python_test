#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

'练习面向对象的高级特性的枚举'

__author__ = 'sergiojune'
from enum import Enum, unique


# 使用枚举
#
Month = Enum('Month', ('Jan', 'Feb',  'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 获取每一个成员，value是自动生成的，从 1 开始
for month,member in Month.__members__.items():
    print(month, '=>', member, member.value)


# 可以继承枚举来实现枚举类
@unique  # 这个装饰器是让枚举的键固定值，并且不能相同
class Weekday(Enum):
    # 这样就实现了枚举类
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问枚举类的值
print(Weekday.Sun)
print(Weekday(1))
print(Weekday['Wed'])
num =4
# 这个访问值
print(Weekday(4).value == num)
# 这个访问键
print(Weekday(4) == num)
for day, member in Weekday.__members__.items():
    print(day, '=>', member)


# 作业：把Student的gender属性改造为枚举类型，可以避免使用字符串
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
