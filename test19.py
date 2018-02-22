#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习面向对象的获取对象的属性和信息'

__author__ = 'sergiojune'

import types

# 判断基本类型
print(type('str'))
print(type(12))
print(type(12.36))


def fn():
    print('fn----')


# 函数类型
print(type(fn))

print(type('d') == str)
print(type(56) == int)
print(type(fn) == types.FunctionType)


class Animal(object):
    def run(self):
        print('run ------')


animal = Animal()
print(type(animal))
# 内置函数类型
print(type(abs))


# 还可以使用isinstance函数来进行判断类型
print(isinstance(123, int))
print(isinstance('dd', str))
# 判断对象类型
print(isinstance([1, 2], list))
print(isinstance({1: 2}, dict))
print(isinstance(fn, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(animal, Animal))
# 第二个参数可以写一个元组。里面的关系表示或
print(isinstance([2, 3, 5], (list, tuple)))


# 对对象的属性进行操作
class MyDog(Animal):
    def __init__(self):
        self.x = 9

    # 这个方法就是调用len函数时被调用的方法
    def __len__(self):
        return 100

    def power(self):
        return self.x * self.x


dog = MyDog()
print(len(dog))
# 获取实例的属性列表
print(dir(dog))
# 获取实例的属性
print(getattr(dog, 'x'))
# 可以设置默认值，当没有时就会返回默认值
print(getattr(dog, 'high', 404))
# 设置属性
setattr(dog, 'high', 0.86)
# 获取上述设置的属性
print(getattr(dog, 'high', 404))
# 还可以判断是否存在该属性
print(hasattr(dog ,'x'))
print(hasattr(dog, 'attr'))

# 还可以获得实例的方法
print(getattr(dog, 'power'))
p = getattr(dog, 'power')
# 下面这个p相当于 dog.power
print(p())
