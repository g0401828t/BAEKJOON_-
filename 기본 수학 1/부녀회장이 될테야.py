# 4   1, 6, 21, 56, 126
# 3   1, 5, 15, 35, 70, ...
# 2   1, 4, 10, 20, 35, ...  
# 1   1, 3, 6, 10, 15, ...  
# 0   1, 2, 3, 4, 5, ...     
import sys

N = int(sys.stdin.readline().strip())
for x in range(N):
    # print("x:",x)
    # print("e:",e)
    k = int(sys.stdin.readline().strip())       # 층
    n = int(sys.stdin.readline().strip())       # 호수

    before = [n for n in range(1, 15)]
    for i in range(k):
        result = 1
        for j in range(1, n):
            result += before[j]
            before[j] = result
    print(before[n-1])
