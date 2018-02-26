#!/ussr/bin/env python 3
# -*- coding: utf-8 -*-

'练习多进程与进程间通信'

__author__ = 'sergiojune'
from multiprocessing import Process, Pool, Queue
import os
import time
from random import random



# print('parent process(%s) is running' % os.getpid())
# 定义子进程需要运行的函数
# def run(name):
#     print('I am runing,I is process(%s)' % os.getpid())
# 在使用这个进程时，需要使用if __name__ == '__main__这个语句来开父进程，要不会出错
# if __name__ == '__main__':
#     # 创建子进程
#     p = Process(target=run, args=('test',))
#     # 开启进程
#     p.start()
#     # 让子进程运行完再运行下面的父进程
#     p.join()
#     print('End...........')



# 使用进程池批量开启进程
# def run(name):
#     print('task %s is running, process %s' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random()*3)
#     end = time.time()
#     print('%s is run %0.2f seconds process %s' % (name, (end - start), os.getpid()))
#
#
# if __name__ == '__main__':  # 开启多进程这个语句是必须的
#     print('parent process %s is running' % os.getpid())
#     # 创建进程池
#     p = Pool(4)
#     for x in range(5):
#         p.apply_async(run, args=(x,))
#     # 关闭进程池，不能再添加进程
#     p.close()
#     # 要实现这个方法之前必须关闭进程池
#     p.join()
#     print('parent process %s end' % os.getpid())



# 实现进程间通信
def write(q):
    print('process %s is writing' % os.getpid())
    for x in 'ABC':
        q.put(x)
        print('   %s write %s' % (os.getpid(), x))


def read(q):
    print('process %s is read' % os.getpid())
    while True:
        value = q.get(True)
        print('info is %s' % value)


if __name__ == '__main__':
    q = Queue()
    print('parent is running')
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 开启进程
    pw.start()
    pr.start()
    pw.join()
    # 由于read方法不能自行停止，所以需要强制tingz
    pr.terminate()
    print('end------')
