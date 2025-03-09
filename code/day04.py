"""
算术运算符

"""
print(100 + 10)     # 加法运算，输出110
print(100 - 10)     # 减法运算，输出90
print(100 * 10)     # 乘法运算，输出1000
print(10 / 3)     # 除法运算，输出3.3333333333333335
print(10 // 3)    # 整除运算，输出3
print(10 % 3)     # 求模运算，取余，输出1
print(3 ** 3)    # 求幂运算，3的3次方，输出27

"""
算术运算的优先级
先乘除后加减，求幂优先于乘除法
"""
print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625

"""
赋值运算符和复合赋值运算符

"""
a = 10
b = 3
a += b        # 相当于：a = a + b，a=13
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么 13*15

"""
海象运算符

"""


"""
比较运算符和逻辑运算符

"""


"""
运算符和表达式

text = input('请输入：')
print(text)
print(type(text))
#f = float(text)
#print(type(f))

"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
'''
%.1f,浮点数保留一位小数

 "... %[key][flags][width][.precision][length type]conversion type ..." % values
conversion type 必选
s	字符串, 使用str()方法转换任何Python对象
d	十进制整数
f	十进制浮点数(小数), 自动保留六位小数。
'''
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
"""
格式化输出 {f:.1f}
"""
