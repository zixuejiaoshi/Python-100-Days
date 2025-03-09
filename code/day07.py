"""
100以内的素数

"""

isPrime = 1
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        isPrime = i
        print(isPrime)



