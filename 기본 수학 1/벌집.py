# 1               => 1
# 2~7             => 6
# 8~19            => 12
# 20~37           => 18
# 38~61           => 24

# n = 6 * (0 + 1 + 2 + ...)


import sys

N = int(sys.stdin.readline())

n = 0
sum = 1
while True:
    sum += (6*n)
    if sum >= N:
        break
    n += 1

print(n+1)
