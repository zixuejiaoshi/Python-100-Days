# 函数
# 输入m和n，计算组合数C(m,n)的值
m = int(input('m = '))
n = int(input('n = '))
# 计算m的阶乘
fm = 1 
for num in range(1, m + 1):
    print(num)
    fm *= num
# 计算n的阶乘  
fn = 1
for num in range(1, n + 1):
    fn *= num
# 计算m-n的阶乘
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
# 计算C(M,N)的值
print(fm // fn // fm_n)

# 输入m和n，计算组合数C(m,n)的值
# 定义一个计算阶乘的函数
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))

# 直接调用已经定义好的函数求阶乘
print(fac(m) // fac(n) // fac(m - n))

# math模块已实现求阶乘函数
from math import factorial
print(factorial(m) // factorial(n) // factorial(m - n))

# 导入函数时可以给函数取别名
from math import factorial as f 
print(f(m) // f(n) // f(m - n))


"""
函数的参数
函数可以有多个参数，也可以没有参数

"""

# 判断三条边的长度能否构成三角形
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b
print(is_triangle(1, 2, 3))
print(is_triangle(2, 3, 4))
print(is_triangle(3, 4, 5))
print(is_triangle(3, 4, 6))

