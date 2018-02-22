#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习面向对象的实例属性和类属性'

__author__ = 'sergiojune'


class Student(object):
    # 这个就是类属性
    name = 'student_name'
    def __init__(self,age):
        # 有self的就是实例属性
        self.age = age


s1 = Student(15)
s2 = Student(16)
# 都是调用类属性
print(Student.name)
print(s1.name)
print(s2.name)
# 修改类属性
Student.name = '_name'
# 全部都变
print(Student.name)
print(s1.name)
print(s2.name)
# 若绑定同名的实例属性到实例中
s1.name = "name_s1"
# 类属性没有变
print(Student.name)
# 同名属性将类属性屏蔽了
print(s1.name)
# 此实例还有类属性
print(s2.name)


# 作业：为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Stu(object):
    num = 0

    def __init__(self,name):
        Stu.num += 1
        self.name = name


s1 = Stu('Bob')
s2 = Stu('Tom')
print(s2.num)
