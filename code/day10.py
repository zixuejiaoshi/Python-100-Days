# tuple 元组，是不可变类型

# 元组的定义
t = (10, 20, 30, 40, 50)
print(t)


# 打包和解包
a = 1, 2, 3
print(a)
print(type(a))

# 解包赋值
a, *b, c = range(10)
print(a, b, c)

a, b, c = (11, 22, 33)
print(a, b, c)

a, b, *c = t    # 用星号表达式修饰的变量会变成一个列表
print(a, b, c)

a, *b, c = t
print(a, b, c)

# 交换两个变量的值
a, b = 10, 20
a, b = b, a
print(a, b)

# 链式赋值
a = b = c = 100
print(a, b, c)
