#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习内建模块之hashlib'

__author__ = 'sergiojune'
import random, hashlib  # 这个包是用于存储数据，防止别人随意修改数据的类，不能用于加密，因为不支持反推明文

s = 'my name is sergiojune'
# 进行MD5保密
md = hashlib.md5()
md.update(s.encode('utf-8'))  # 指定编码方式
# 获取加密后的值
print(md.hexdigest())
# 修改一点内容后
s = 'my name is june'
md5 = hashlib.md5()
md5.update(s.encode('utf-8'))
print(md5.hexdigest())  # 通常结果是128位的bit，用32位的16进制表示


# 使用sha1，用法与md5一样
sha = hashlib.sha1()
sha.update(s.encode('utf-8'))
print(sha.hexdigest())  # 结果是160位的bit，用40位的16进制表示

# 作业1：设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, passwd):
    m = hashlib.md5()
    m.update(passwd.encode('utf-8'))
    return db[user] == m.hexdigest()


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# 作业2：根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    password = password + user.salt
    return user.password == get_md5(password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
