# 练习python的参数

# 命名关键字参数，与默认参数有点不同，这个参数没有默认值，而且也属于必填参数，不填时会报错
def fun(name,age,*,city,job):
    print(name,age,city,job)

fun('huang',15,city='biejing',job='progrommer')



# 参数下的练习题
def product(*nums):
    if nums is None:
        raise TypeError('参数不能为None')
    res = 1
    for num in nums:
        res *= num

    return res
