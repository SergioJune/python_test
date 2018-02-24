#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习序列化和反序列化'

__author__ = 'sergiojune'
import pickle
import json
d = {'name': 'bob', 'age': 20, 'score': 80}
# 序列化,这个是序列化成bytes
p = pickle.dumps(d)
print(p)
# 这个序列化后直接存在指定文件
with open('pickle.txt', 'wb') as f:
    pickle.dump(d, f)

# 反序列化
# 这个是将bytes反序列化
p = pickle.loads(p)
print(p)
# 这个是将文件反序列化
with open('pickle.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)


# 若要在个语言之间相互传递对象，这时就需要序列化成JSON或XML等格式
# 这里序列化成JSON，用的是json库
d = {'name': 'bart', 'age': 22, 'score': 76}
j = json.dumps(d)
print(j)
# 序列化后写入文件
with open('json.txt', 'w') as f:
    json.dump(d, f)
# 反序列化
f = json.loads(j)
print(f)
# 从文件中反序列化
with open('json.txt', 'r') as f:
    w = json.load(f)
    print('文件：', w)


# 序列化自定义类
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self. age = age
        self.score = score


s = Student('tom', 23, 68)
# 这个是获取对象的字典形式
print(s.__dict__)
# 直接序列化会出错，抛TypeError: Object of type 'Student' is not JSON serializable，说该对象不可序列化
# o = json.dumps(s)
# 对自定义对象序列化需要自己先将对象转换成字典才能序列化


# 将student转换成字典
def student2dict(obj):
    return {'name': obj.name,
            'age': obj.age,
            'score': obj.score}


# 现在序列化
o = json.dumps(s, default=student2dict)
print(o)
# 可以利用类的特性和匿名函数一行代码进行序列化
o1 = json.dumps(s, default=lambda obj: obj.__dict__)
print('简易序列化', o1)

# 反序列化


# 在自定义类中，同样也需要加个函数将序列化后的字典转换成对象的对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


fan = json.loads(o, object_hook=dict2student)
# 这样就获取到student对象
print(fan)


# 作业：对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响
obj = dict(name='小明', age=20)
# 当ensure_ascii为True，会对中文进行编码
s = json.dumps(obj, ensure_ascii=True)
print(s)
# 当ensure_ascii为False，不会对中文进行编码
s = json.dumps(obj, ensure_ascii=False)
print(s)
