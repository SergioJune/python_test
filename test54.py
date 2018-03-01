#!/usr.bin.env python 3
# -*- coding: utf-8 -*-

'''
练习python的asyncio
'''

__author__ = 'sergiojune'
import asyncio,threading


@asyncio.coroutine  # 这个装饰器是把生成器标记成为coroutine
def hello():
    r = ''
    print('hello world(%s)' % threading.current_thread())
    n = yield from asyncio.sleep(1)  # 这个方法也是个coroutine,执行到这里后会等待该方法返回数给这个coroutine
    print('hello again(%s)' % threading.current_thread())


# 这是练习一个协程的
# # 获取事件循环，就是eventloop
# loop = asyncio.get_event_loop()
# # 执行coroutine,参数是需要运行的协程
# loop.run_until_complete(hello())
# # 关闭
# loop.close()


# 这个执行两个hello
# l = asyncio.get_event_loop()
# # 把协程放到eventloop里面
# # 这两个方法是并发执行的
# l.run_until_complete(asyncio.wait([hello(), hello()]))  # wait()是将参数里的协程转为一个包括他们在内的单独协程
# l.close()


# 练习用异步连接新浪搜狐和网易云
def wget(host):
    print('ready ro connect %s' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect  # 这个io操作比较耗时，所以会执行下个协程
    header = 'GET/HTTP/1.1\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()  # 用于刷新缓存区的内容，确保将内容提交上去
    while True:
        line = yield from reader.readline()  # 这个io操作有时不耗时，会直接运行整个循环
        if line == b'\r\n':
            break
        print('%s header>%s' % (host, line.decode('utf-8').strip()))
    writer.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]))
loop.close()
