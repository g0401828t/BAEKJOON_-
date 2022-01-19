import math


N = int(input())

# N = 5x + 3y

# x = N//5
# remain = N%3


result = math.inf
total = 0
count_5 = 0
count_3 = 0
for i in range(N//5 + 1):
    count_5 = i
    remain = N - (5*i)
    total += i
    while remain > 0:
        count_3 += 1
        remain -= 3
        total += 1
    
    if result >= total and remain == 0:
        result = total
    count_5 = 0
    count_3 = 0
    total = 0

if result == math.inf:
    print(-1)
else:
    print(result)
