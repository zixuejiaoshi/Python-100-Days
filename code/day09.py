# 列表生成式
# 创建一个取值范围在`1`到`99`且能被`3`或者`5`整除的数字构成的列表。

items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

# 有一个整数列表`nums1`，创建一个新的列表`nums2`，`nums2`中的元素是`nums1`中对应元素的平方。
nums1 = [1, 2, 3, 4, 5]
nums2 = [i ** 2 for i in nums1]
print(nums2)

# 有一个整数列表`nums1`，创建一个新的列表`nums2`，将`nums1`中大于`50`的元素放到`nums2`中。
nums1 = [1, 2, 3, 4, 5, 60, 70, 80, 90, 100]
nums2 = [i for i in nums1 if i > 50]
print(nums2)

# 嵌套列表
# 创建一个嵌套列表，每个元素是一个长度为`3`的列表，每个列表中的元素都是`0`到`9`的随机整数。
import random

nums = [[random.randint(0, 9) for j in range(3)] for i in range(3)] 
print(nums)
