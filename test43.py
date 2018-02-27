#!/usr/bin/env python3
# -*- conding: utf-8 -*-

'练习内建模块之hmac'

__author__ = 'sergiojune'
import random, hmac  # 这个模块是可以根据口令进行加密保存数据，相当于md5加slat的效果，还比他强
message = b'hello world'
key = b'key'
# 第一个和第二个参数都必须是bytes类型
p = hmac.new(key, message, digestmod='md5')  # 指定md5算法，一个参数为口令，第二个为加密的信息
print(p.hexdigest())


# 作业：将上一节的salt改为标准的hmac算法，验证用户口令
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
