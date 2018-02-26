#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习分布式进程 '

__author__ = 'sergiojune'
import queue, random
from multiprocessing.managers import BaseManager
# 此文件用来发送和接受结果，test36.py用于处理结果

# 创建通信工具
# 发送任务
post_task = queue.Queue()
# 接受结果
result_task = queue.Queue()


class QueueManager(BaseManager):
    pass


# 定义的函数解决下面的坑
def posttq():
    return post_task


def resulttq():
    return result_task


def start():
    # 注册任务
    # 这里有个坑，在window系统下callable不能为匿名函数，原因是不能被序列化，所以在这里我们需要定义函数
    QueueManager.register('post_task_queue', callable=posttq)  # 第一个参数为注册名字
    QueueManager.register('result_task_queue', callable=resulttq)

    # 绑定窗口，设置验证码
    manager = QueueManager(address=('127.0.0.1', 500), authkey=b'abc')  # 第一个参数为地址和端口，第二个参数为验证码，防止别人骚扰

    # 启动管理
    manager.start()
    # 通过管理器获取通信
    post = manager.post_task_queue()
    result = manager.result_task_queue()

    # 进行发送数据
    print('try post data')
    for x in range(10):
        n = random.randint(1, 1000000)
        print('put %d' % n)
        post.put(n)

    # 接受结果
    print('try get result')
    for x in range(10):
        # timeout表示超时获取数的最长时间
        value = result.get(timeout=10)
        print('get result', value)

    # 关闭管理器
    manager.shutdown()
    print('master end')


if __name__ == '__main__':
    start()
