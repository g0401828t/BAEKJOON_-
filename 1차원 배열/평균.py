import sys

N = int(sys.stdin.readline())
Data = list(map(float, sys.stdin.readline().split()))

M = max(Data)
result = 0
for data in Data:
    data = data / M * 100
    result += data / N

print(result)

