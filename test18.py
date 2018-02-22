#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习面向对象的继承和多态'

__author__ = 'sergiojune'


class Animal(object):
    def run(self):
        print('animal is running')


# 继承Animal类
class Dog(Animal):
    # 重载父类的方法
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('cat is running')


def run_twich(animal):
    animal.run()
    animal.run()


animal = Animal()
dog = Dog()
cat = Cat()
# 类继承了Animal，所以类中不需要实现任何东西都可以有父类方法
animal.run()
dog.run()
cat.run()
# 这个方法只要是有run方法都可以运行,这就是多态的实现
# 看起来像鸭子，走起路来像鸭子，那这个就是鸭子，这就是鸭子类型，动态语言的鸭子类型
run_twich(animal)
run_twich(dog)
run_twich(cat)
