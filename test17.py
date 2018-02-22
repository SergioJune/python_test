#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习面向对象的访问限制'

__author__ = 'sergiojune'

# 定义实例
class Student(object):
    def __init__(self, name, score):
        # 前面带了两个下划线表示对变量进行私有化，让外部不可以随意访问和修改
        # 但这个只是意识上私有而已，因为在外部我们可以通过 _类名__变量名 来访问，但不建议这样做，因为不同版本名字或许不一样
        # 所以私有了，一切靠自觉
        self.__name = name
        self.__score = score

    def get_grade(self):
        print('my name is %s,my grade is %d' % (self.__name,self.__score))

    # 当外界需要获取时，可以单独写一个方法来获取和设置
    # 这样做的好处就是使用户不能随意修改，因为是方法，所以可以实现一些逻辑判断
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            raise ValueError('请输入正确名字')

    def set_score(self,score):
        if isinstance(score,int):
            self.__score = score
        else:
            raise ValueError('请输入正确的成绩')


# 实例化
bart = Student('Bart', 89)
bart.get_grade()
print(bart.get_name())
bart.set_score(56)
print(bart.get_score())
# 这样访问私有变量,显然正确，但不推荐这样做
print(bart._Student__name)
# 但是你这样设置变量就错了
bart.__name = 'new name'  # 这样做只是给这个实例添加了__name 的属性，并不是修改了私有变量
print(bart.get_name())  # 可以看出这个名字还是不变


# 作业：把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
class StudentA(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_name(self,name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError('请输入字符串的名字')

    def set_gender(self,gender):
        if isinstance(gender, str):
            self.__gender = gender
        else:
            raise ValueError('请输入正确性别')


# 检验是否正确
bart = StudentA('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')