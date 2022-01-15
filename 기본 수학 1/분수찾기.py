# 1 => 1
# 2 => 2 3
# 3 => 4 5 6
# 4 => 7 8 9 10


import sys

N = int(sys.stdin.readline())

n = 1
sum = 0
while True:
    sum += n
    if sum >= N:
        break
    n += 1

i = sum - N # 마지막 분수에서 얼마나 떨어져있는지
# 양수번째 줄일때 마지막 분수 = 2/1, 4/1, 6/1, ...
if n%2 == 0:
    print("{}/{}".format(n-i, 1+i))
# 음수번째 줄일때 마지막 분수 = 1/1, 1/3, 1/5, ...
else:
    print("{}/{}".format(1+i, n-i))
