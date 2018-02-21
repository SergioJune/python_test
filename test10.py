# 练习函数式编程的sorted函数


L = [1, 5, 6, 9, -8, 7, -4, -1, 3, -5]
print(L)
# 排序不改变原来函数，生成一个新的列表
L = sorted(L)
print(L)
# 指定排序方式
L = [1, 5, 6, 9, -8, 7, -4, -1, 3, -5]
L = sorted(L, key=abs)
print(L)

s = ['dfs','Fds','tda','Eds']
print(s)
print(sorted(s))
print(sorted(s, key=str.lower))
# 反向排序
print(sorted(s, key=str.lower, reverse=True))


# 作业：假设我们用一组tuple表示学生名字和成绩，L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]，按名字进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda x: x[0]))
# 按成绩进行排序
print(sorted(L,key=lambda x: x[1]))
