#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'udp配合test51文件的服务器，这文件当作客户端'

__author__ = 'sergiojune'
import socket

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# UDP协议不需要建立连接
for x in [b'bret', b'tom', b'sergiojune']:
    s.sendto(x, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
