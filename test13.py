# 练习函数式编程的装饰器
from functools import wraps
import time


# now()
# 现在想在函数里面增加打印log信息，这时又不想修改函数内部，此时可用装饰器
def decorator(func):
    @wraps(func)  # 加这个装饰器是将原函数的__name__等属性复制到这个wrapper函数，防止某些依赖函数签名的代码发生错误
    def wrapper(*args, **kw):
        print('%s %s()' % ('decorator', func.__name__))
        func()
    return wrapper


@decorator
def now():
    print('2018-02-22')


now()  # 加了装饰器之后再调用该函数就是装饰器里的wrapper()函数内容了
# 在装饰器上也加个wraps装饰器后就可以复制原函数的属性了，此时就变成了原函数名字
print(now.__name__)  # 此时他的__name__属性也改变了


# 有参数的装饰器
def log(text):
    def decorator(func):
        @wraps(func)  # 记得加这个装饰器防止错误
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__,))
            func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def fun():
    print('now:2018-02-22')


fun()
print(fun.__name__)


# 作业：设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print(time.time())
        return func(*args, **kw)
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


print('作业')
print(fast(11, 22))
print(slow(11, 22, 33))
