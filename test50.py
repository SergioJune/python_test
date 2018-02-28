#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'配合test49文件的服务器，这文件当作客户端'

__author__ = 'sergiojune'
import socket

# 建立socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接地址
s.connect(('127.0.0.1', 9999))
# 接受返回的数据
print(s.recv(1024).decode('utf-8'))
# 发送数据
for x in [b'bob', b'amy', b'june']:
    print('send %s' % x)
    s.send(x)
    print(s.recv(1024).decode('utf-8'))
# 发送退出数据
s.send(b'exit')
s.close()
print('connect is closed from kehuuduan')
