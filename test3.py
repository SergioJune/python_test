# 练习列表的切片
# 切片是产生一个新的列表，不会修改原来的列表


l = ['john','miss','mike','jack','amy']
# 获取前三位元素,切片一样包头不包尾
print(l[0:3])
# 获取后三位元素
print(l[2:])
# 支持负数的哈，往后数第一个为-1
print(l[-3:])
# 完全复制一个列表
print(l[:])
# 按步长来取元素,步长为2
print(l[::2])

# tuple也可以切片操作
t=(1,2,3,4,5,78,9,10)
print(t[::3])

# 而字符串也支持切片操作，因为他也是一个序列
s = 'sergiojune'
print(s[-4:])


# 作业：利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(str):
    n1 = 0
    n2 = len(str)-1
    for num in range(len(str)):
        if str[num] == ' ':
            continue
        else:
            n1 = num
            break
    for num in range(n1,len(str),-1):
        if str[num] == ' ':
            continue
        else:
            n2 = num
            break
    return str[n1:n2+1]


# 上述方法较复杂，参考了别人的写法，重新写
def trim2(str):
    while True:
        if str[0] == ' ':
            str = str[1:]
        else:
            break
    while True:
        if str[-1] == ' ':
            str = str[0:-1]
        else:
            break

    return str


s = '  hello  world   '
print(trim2(s))