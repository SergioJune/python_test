#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习多线程'

__author__ = 'sergiojune'
import threading
import multiprocessing


def run():
    print('thread %s is running' % threading.current_thread().name)
    for x in range(5):
        print('thread %s ==> %d' % (threading.current_thread().name, x))
    print('thread %s end' % threading.current_thread().name)


print('thraed %s is running' % threading.current_thread().name)
t = threading.Thread(target=run, name='loopthread')
# 开启线程
t.start()
t.join()
print('thread %s is end' % threading.current_thread().name)


# 多线程的锁
balance = 0
def change(n):
    global balance
    balance = balance + n
    balance = balance - n
    print(balance)


def run_thread():
    l = threading.Lock()
    for x in range(1, 100000):
        try:
            # 获取锁
            l.acquire()
            change(x)
        finally:
            # 释放锁
            l.release()


t1 = threading.Thread(target=run_thread)
t2 = threading.Thread(target=run_thread())
t1.start()
t2.start()
t1.join()
t2.join()
print('end')


def loop():
    x = 0
    while True:
        x = x ^ 1


for x in range(multiprocessing.cpu_count()):  # 根据cpu的数量来开线程
    t = threading.Thread(target=loop)
    t.start()

