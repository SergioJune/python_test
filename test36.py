#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'处理分布式进程发送的数据'

__author__ = 'sergiojune'
from multiprocessing.managers import BaseManager
import time, queue


class QueueManager(BaseManager):
    pass


# 注册到网络上
QueueManager.register('post_task_queue')  # 由于只是从网络上获取queue，所以不需要写callable方法
QueueManager.register('result_task_queue')
# 连接到网络
address = '127.0.0.1'  # 这个是网络地址
manager = QueueManager(address=(address, 500), authkey=b'abc')  # 这些必须与发送的一致，要不会连不上
# 连接
manager.connect()
# 获取queue
post = manager.post_task_queue()
result = manager.result_task_queue()

# 处理数据
print('tyr get value')
for x in range(10):
    try:
        v = post.get(timeout=10)
        print('get value %d' % v)
        r = v*v
        print('put value %d to result' % r)
        time.sleep(1)
        result.put(r)
    except queue.Empty as e:
        print('Queue is empty')
print('work exit')
