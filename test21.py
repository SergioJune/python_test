#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习面向对象高级特性的__slots__属性'

__author__ = 'sergiojune'
from types import MethodType

class MyObject(object):
    pass


o = MyObject()
# 动态绑定属性
o.name = 'object'
print(o.name)


# 也可以动态绑定方法
def get_info(self):
    print('动态绑定的方法')


o.get_info = MethodType(get_info, o)
o.get_info()
# 动态绑定的方法和属性对其他实例无效
oo = MyObject()
# oo.get_info()
# 此时可以动态绑定在类中
MyObject.get_info = get_info
# 这样就可以了
oo.get_info()


# 为了防止用户乱绑定属性，python中加了个__slots__属性，来限制动态绑定的属性
class Student(object):
    # 值是一个元组。里面表示的是可以动态绑定的属性
    __slots__ = ('name', 'age')

    def __init__(self,name):
        self.name = name


s1 = Student('Bob')
s1.age = 100
print(s1.age)
# 下面这个就会报错：AttributeError: 'Student' object has no attribute 'scoer'
# s1.scoer = 85
# 绑定方法也会报同样的错误
# s1.get_info = MethodType(get_info, s1)


# 使用了__slots__属性时，其子类不受限制
class MyStudent(Student):
    pass


m = MyStudent('bart')
# 这个就不会报错，要想限制也需要单独加那个属性
m.score = 100


