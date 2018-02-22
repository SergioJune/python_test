# 练习下函数式编程的返回函数


# 在python中，函数可以当返回值返回
def func(*args):
    # 求可变参数的和
    def fun():
        sum = 0
        for n in args:
            sum += n
        return sum
    return fun


# 上述的就是闭包，闭包中内层函数可以使用外层函数的变量
sum = func(*[1, 3, 5, 7, 9])
print(sum)  # 可以看出返回了一个函数，内层函数
print(sum())  # 若要输出结果就是加个小括号就可，这种是惰性求和


# 但是在使用循环变量时
def f1():
    fs = []
    for x in range(1, 4):
        def f2():
            return x*x
        fs.append(f2)
    return fs


# 上面利用循环返回了一个存有三个函数的列表，现在一一复制看结果
n1, n2, n3 = f1()
# 可以看出，结果都是三，并不是想象中的1，4，9
# 这是因为我们在使用闭包时，内层函数的变量指向了循环变量，而函数并不是立即执行，当循环完后，循环变量就变了，这时再执行函数就会产生意想不到的结果
# 所以在使用闭包时记得尽量不要使用循环变量
print(n1())
print(n2())
print(n3())


# 若一定要使用循环变量，就是在内层函数在定义一个函数来绑定循环变量让他不再可变
def f1():
    def f2(i):
        def f3():
            return i*i
        return f3
    fs = []
    for x in range(1, 4):
        fs.append(f2(x))

    return fs


# 现在就可以了使用循环变量了
n1, n2, n3 = f1()
print(n1())
print(n2())
print(n3())


# 闭包还可以这样玩，用闭包来求泛型函数
def line(a, b):
    # 内层函数也加了个参数
    def aline(x):
        return a*x + b
    return aline


l1 = line(2,3)
l2 = line(5,6)
# 求值时因为内层函数需要传参数，所以这里也需要传参数
print(l1(3))
print(l2(8))


# 作业：利用闭包返回一个计数器函数，每次调用它返回递增整数
def create_count():
    # 将变量n设为全局变量
    global n
    n = 0

    def counter():
        # 将变量n设为全局变量
        global n
        n += 1
        return n
    return counter


counter = create_count()
print(counter(), counter(), counter(), counter(), counter())
countera = create_count()
print(countera(), countera(), countera(), countera(), countera())

