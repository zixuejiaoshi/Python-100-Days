"""
list 列表 — 常用数据结构

"""

items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
items4 = list(range(10))
items5 = list('hello')

# 列表的运算

# 列表的拼接
print(items1 + items5)

# 列表的重复
print(items2 * 3)

# 列表的成员运算
print(12 in items1)
print(12 not in items1)

# 列表的长度
print(len(items1))

# 列表的索引和切片
print(items1[2])    # 取第三个元素
print(items1[-1])   # 取最后一个元素
print(items1[1:3])  # 取第二个到第三个元素
print(items1[1:])   # 取第二个到最后一个元素

print(items1[0:3:1])  # 取第一个到第三个元素，步长为1

# 列表的修改
items1[2] = 100 
items1[2] += 1   # 修改第三个元素
print(items1)

items1[1:3] = [200, 300]   # 修改第二个到第三个元素

# 列表的删除
del items1[2]
print(items1)

# 列表的方法
items1.append(100)  # 在末尾添加元素
print(items1)   
items1.insert(1, 200)   # 在指定位置添加元素
print(items1)   
items1.extend([100, 200, 300])  # 在末尾添加多个元素
print(items1)
items1.remove(100)  # 删除指定元素
print(items1)
items1.pop()    # 删除末尾元素
print(items1)
items1.pop(0)   # 删除指定位置元素
print(items1)

# 列表的排序
items1.sort()   # 升序排序
print(items1)
items1.sort(reverse=True)   # 降序排序
print(items1)

# 列表的反转
items1.reverse()
print(items1)

# 列表的复制
items6 = items1.copy()
print(items6)

# 列表的清空
items1.clear()
print(items1)

# 列表的遍历
for item in items2:
    print(item)

items1.count(35)    # 统计元素出现的次数

"""
将一颗色子掷6000次，统计每种点数出现的次数

"""

import random

dice = [0] * 6   # 初始化一个长度为6的列表，每个元素的值为0

for i in range(6000):
    face = random.randint(1, 6)     # 随机生成一个点数
    dice[face - 1] += 1     # 统计每个点数出现的次数

for i in range(6):
    print(f'{i + 1}点出现了{dice[i]}次')
