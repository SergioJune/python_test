#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 练习面向对象的类和实例 '

__author__ = 'sergiojune'

# 定义学生实例


class Student(object):
    def __init__(self, name, score):
        ' 初始化实例，当创建实例时被调用这个函数，所以在实例化时需要传入这个函数的参数 '
        self.name = name
        self.score = score

    def get_grade(self):
        '对数据进行封装'
        print('my name is %s' % self.name)
        if self.score > 90:
            print('your grade is A')
        elif self.score > 75:
            print('your grade is B')
        else:
            print('your grade is C')


# bart = Student()
# print(bart)
# # 给实例初始化名字属性和成绩
# bart.name = 'bart june'
# bart.score = 98
# print(Student)
# print(bart.name)
# print(bart.score)
# 实例化
tom = Student('Tom', 87)
print(tom.name)
print(tom.score)
bob = Student('Bob', 65)
# 调用实例方法
bob.get_grade()
