#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'用于练习网络编程TCP'

__author__ = 'sergiojune'
import socket, threading, time

# 创建socket
# s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  # 第一个参数为指定ipv4模式， 第二个参数指定为tup模式的面向流
# # 建立连接
# s.connect(('www.sina.com.cn', 80))
# # 发送请求
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')  # 发送get请求，http协议
# # 处理返回来的数据
# buffer = []
# while True:
#     # 指定最大接受1024个字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# # 关闭连接
# s.close()
# 取出请求头和内容
# header, body =data.split(b'\r\n')
# print(header)
# print(body)


# 建立服务器端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口和地址，当有信息从这个端口发送过来时就捕捉
s.bind(('127.0.0.1', 9999))  # 这个为本机ip，这个服务器只能接受本地的
# 监听窗口
s.listen(5)  # 传入参数为最大的等待连接数
print('await for connect')
def tcplink(sock, add):
    print('here is a connector from %s:%s' % add)
    # 向客户端发送数据
    sock.send(b'Welcome')
    # 处理客户端发送来的数据
    while True:
        d = sock.recv(1024)
        time.sleep(1)
        if not d or d == b'exit':
            break
        sock.send(('hello %s !' % d.decode('utf-8')).encode('utf-8'))
    # 关闭连接
    sock.close()
    print('connect is closed')

# 用永久循环来等待客户端连接
while True:
    # 这个函数会返回一个客户端连接
    sock, add = s.accept()
    # 创建线程来处理客户端的数据
    t = threading.Thread(target=tcplink, args=(sock, add))
    # 开启线程
    t.start()
