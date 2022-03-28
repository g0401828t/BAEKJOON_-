import sys

N = int(sys.stdin.readline())

data = []
for n in range(N):
    data.append(list(map(str, sys.stdin.readline().split())))

data.sort(key=lambda x:int(x[0]))


for d in data:
    print(d[0], d[1])
