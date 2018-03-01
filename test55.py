#!/usr.bin.env python 3
# -*- coding: utf-8 -*-

'''
练习python的async/await
async:相当于asyncio.coroutine,可以用这个替换这个更加方便
await:相当于yield form，把这个改成await即可替代
以上都是在python3.5版本以上才有的
'''

__author__ = 'sergiojune'
import asyncio


async def hello():  # 这样就是相当于一个coroutine了
    print('hello world')
    await asyncio.sleep(1)
    print('hello again')


# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


# 两个协程
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([hello(), hello()]))
# loop.close()


# 再用这个方法连接搜狐新浪和网易
async def wegt(host):
    print('wegt %s ' % host)
    # 连接
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET/HTTP/1.0\r\nHost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()  # 相当于刷新缓存
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            print()
            break
        print('%s header > %s' % (host, line.decode('utf-8').strip()))
    connect.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([wegt(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]))
loop.close()
