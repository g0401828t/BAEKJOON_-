import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

data.sort()

for i in data:
    print(i)
