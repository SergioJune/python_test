#!/usr.bin.env python 3
# -*- coding: utf-8 -*-

'''
练习python的aiohttp
练习服务器上的异步操作
'''

__author__ = 'sergiojune'
import asyncio
from aiohttp import web


async def index(request):  # 首页返回一个h1标签
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>index</h1>', content_type='text/html')


async def hello(request):  # 根据url参数返回信息
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>hello %s</h1>' % request.match_info['name'], content_type='text/html')


# 初始化服务器,也是一个coroutine
async def init(loop):  # 接受协程池
    app = web.Application(loop=loop)
    # 添加反应路径
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    s = loop.create_server(app.make_handler(), '', 80)  # 用loop.create_server创建tcp协议
    print('sever is start in 127.0.0.1:80')
    return s


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()  # 服务器永远运行

