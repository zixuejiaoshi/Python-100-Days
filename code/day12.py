# 集合

set1 = {}
print(set1)

set2 = {1, 2, 3, 3, 2}
print(set2)

set3 = set('hello')
print(set3)

set4 = set([1, 2, 3, 3, 2])
print(set4)

set5 = set(range(6))
print(set5)

set6 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set6)

set7 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set7)
