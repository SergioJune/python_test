#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

'练习面向对象的高级特性的定制类'

__author__ = 'sergiojune'


class Fib(object):
    # 在实例化时会调用该方法
    def __init__(self):
        self.name = 'Fib'
        self.a = 0
        self.b = 1

    # 在调用len方法时实际调用的是该方法
    def __len__(self):
        return 100

    # 在打印实例信息时调用该方法
    def __str__(self):
        return 'object name is %s' % (self.name)

    # 因为一般这两个方法代码一样，所以这样做
    __repr__ = __str__

    # 这个方法让实例可迭代,返回的是一个可迭代对象
    def __iter__(self):
        return self

    # 这个方法当实例用于for循环时会被调用，与list，tuple类似
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        # 到达指定数目就返回一个异常
        if self.a > 100000:
            raise StopIteration
        return self.a

    # 该方法当实例在用下标取元素时被调用,传入切片也是调用这个函数
    # 该方法也可以像dict那样用键来获取值，判断参数是否是字符串即可
    def __getitem__(self, num):
        # 对参数进行判断
        if isinstance(num, slice):
            start = num.start
            end = num.stop
            step = num.step
            # 开头可能不填
            start = start if start else 0
            # 步长也一样
            step = step if step else 0
            L = []
            if step == 0:
                for x in range(start, end):
                    L.append(Fib()[x])
            else:
                for x in range(start, end, step):
                    L.append(Fib()[x])
            return L
        else:
            n = 0
            for x in Fib():
                if n == num:
                    return x
                n += 1

    # 该方法当用下标设置对应值时被调用，也可以像dict一样的赋值
    def __setitem__(self, index, value):
        # 和上面的差不多，就不实现了
        pass

    # __delitem__():方法是当删除某个值时就会被调用


fib = Fib()
print(len(fib))
# 打印实例
print(Fib())
# 打印有变量指向的实例信息
print(fib)
# 用类实现斐波那契数列
for x in fib:
        print(x)
print('-----------')
print(fib[5])
# 切片
print(fib[1:5])
# 有步长
print(fib[5:1:-2])


class Student(object):
    def __init__(self, name):
        self.name = name

    # 这个方法当实例方法不存在的属性时被调用
    def __getattr__(self, name):
        if name == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % name)

    # 这个方法就是当实例当函数被调用时调用这个方法,还可以传参数
    def __call__(self):
        print('call Student')


stu = Student('bart')
print(stu)
# 访问不存在的属性,加了__getattr__方法后就不会报错
print(stu.score)
# print(stu.j)
# 将实例当函数调用
stu()
# 判断对象是否可被调用
print(callable(stu))
print(callable([1]))
print(callable(fib))


# 实现教程中的Chain().users('michael').repos 得到  GET /users/:user/repos
class Chain():
    def __init__(self, path='GET'):
        self.path = path

    def __getattr__(self, path):
        if path:
            return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    def __call__(self, user):
        return Chain('%s/:%s' % (self.path, user))


chain = Chain()
print(Chain().users('michael').repos)
