'''
循环结构
'''



import time
for i in range(1, 3):
    print('hello world')
    time.sleep(1)

# 对于不需要用到循环变量的`for-in`循环结构，
# 按照 Python 的编程惯例，我们通常把循环变量命名为`_`
for _ in range(3):
    print('hello world')
    time.sleep(1)

'''
while 循环
'''
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

'''
break 和 continue 语句
'''
totalTwo = 0
i = 2
while True:
    totalTwo += i
    i += 2
    if i > 100:
        break
print(totalTwo)

