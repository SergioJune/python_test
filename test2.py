# 练习python的递归函数


# 用递归来求阶乘
def func(num):
    if num == 1:
        return 1
    return func(num-1)*num


# 求100的阶乘
num = 100
n = func(num)
print('%d的阶乘是' % (num,), n)


# 上面的函数如果n的数字过大的话就会出现栈溢出的问题，这是我们需要通过尾递归来优化
def fact(num, product=1):
    if num == 1:
        return product
    return fact(num-1, num*product)


# 虽然做了尾递归优化，但是该语言底层没有弄优化，所以还是求不了1000的阶乘
num = 500
n = fact(num)
print('%d的阶乘是' % (num,), n)


# 最后的作业，练习汉诺塔：move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        # 借助c柱将a的移动到c
        move(n-1, a, c, b)
        # 借助b柱将a的最后一根移动到c
        move(1, a, b, c)
        # 最后将b柱的借助a柱移动到c柱
        move(n-1, b, a, c)


move(3, 'A', 'B', 'C')

