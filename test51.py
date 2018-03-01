#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习UDP网络协议'

__author__ = 'sergiojune'
import socket

# 此文件用于当服务器
# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 第二个参数为指定udp协议
# 绑定端口，不需要监听
s.bind(('127.0.0.1', 9999))
print('await connect')
while True:
    data, addr = s.recvfrom(1024)  # 这个直接返回客户端的ip和请求信息
    print('connect form %s:%s' % addr)
    # 发送数据回客户端
    s.sendto(b'hello %s' % data, addr)  # 第二个参数为发送到的ip
