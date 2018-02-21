# 练习函数式编程的filter过滤器
from functools import reduce


L = [x for x in range(100)]
# 过滤取3的倍数
L = filter(lambda x: x % 3 == 0, L)  # 这个返回也是一个迭代器，可以通过next来获取下一个元素
print(next(L))
# 转成list
print(list(L))


# 获取初始序列,因为偶数都不是素数，所以就只有奇数
def get_list():
    n = 1
    while True:
        n = n+2
        yield n


# 获取素数
def get_primes():
    num = 2
    yield num
    # 初始化序列
    it = get_list()
    while True:
        num = next(it)
        yield num
        # 排除第一个数的倍数
        filter(lambda x: x % num != 0, it)


for num in get_primes():
    if num < 1000:
        print(num)
    else:
        break


# 作业：回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    l = list(str(n))
    l.reverse()
    num = reduce(lambda x, y: int(x) * 10 + int(y), l)
    return num == n


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
