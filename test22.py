#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习面向对象高级特性的@property'

__author__ = 'sergiojune'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError('请输入正确的名字')
        self.__name = name

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('请输入正确的成绩')
        elif not isinstance(score, int):
            raise ValueError('请输入正确的成绩')
        else:
            self.__score = score


stu = Student('bob', 86)
print(stu.get_name())
# 这个就会报错
# stu.set_score(999)


# 使用@property装饰器
class People(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # 添加装饰器，让这个方法变成一个属性
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter  # 这个前缀名字要和property装饰器的方法名字一致
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError('请输入正确名字')
        self.__name = name


p = People('bart', 20)
# 加了装饰器之后这样直接调用属性
print(p.name)  # 这个就是直接获取name属性
p.name = 'bat'  # 直接修改属性
print(p.name)
print(p.age)
# 由于age只是只读，不予许写，所以这个会报错
# p.age = 52


# 作业：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    def __init__(self):
        self.__width = None
        self.__height = None

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self,width):
        if width < 0 or width > 1000:
            raise ValueError('请输入正确的宽')
        self.__width = width

    @height.setter
    def height(self, height):
        if height < 0 or height > 1000:
            raise ValueError('请输入正确的高')
        self.__height = height

    @property
    def resolution(self):
        self.__resolution = (self.__height, self.__width)
        return self.__resolution


screen = Screen()
screen.width = 25
screen.height = 65
print(screen.width)
print(screen.height)
print(screen.resolution)
