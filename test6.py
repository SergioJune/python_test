# 练习生成式，生成式就是将列表生成式的中括号改成小括号即可


g = (x for x in range(1,20))
print(g)  # 这是个generator对象
print(next(g))  # 不断使用next来进行获取下一个数，当获取到最后一个数时会抛出StopIteration错误
# 可见这种方法对于列表相当大时，就可以节约内存，同时他也可以用for循环来获取元素
for x in g:
    print(x)


# 使用yield来定义一个生成器的函数
def odd():
    print('yield 1')
    # yield就是一个关键字，用来生成生成器
    # 每执行一个next函数时，就会运行到一个yield处，把该值返回
    yield 1
    print('yield 2')
    yield 2
    print('yield 3')
    yield 3


o = odd()
# 他是生成器，所以可以通过next来获取数
print(next(o))
print(next(o))
print(next(o))
# next(o)


# 使用yield来编写斐波那契数列
def fib(n):
    a, b = 0, 1
    while n > 0:
        # 第一和第二个数都是1
        yield b
        a, b = b, a+b
        n -=1
    return 'done'


num = fib(6)
# 因为是生成器，所以可以通过for循环来获取元素
for x in num:
    print(x)


# 作业：有一个杨辉三角，把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles(n):
    l = [1]
    # 记录第几行，同时知道有多少个元素
    num = 1
    while num <= n:
        # 使用切片是避免两个变量指向同一个列表，从而影响了下面操作
        L = l[:]
        yield L
        num += 1
        if len(l) > 1:
            for d in range(1, num-1):
                l[d] = L[d] + L[d-1]
        l[0] = 1
        l.append(1)


t = triangles(10)
for x in t:
    print(x)