import sys


N = int(input())

for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    
    mu = sum(data[1:]) / data[0]
    
    count = 0.0
    for n in data[1:]:
        if n > mu:
            count += 1

    print("{:.3f}%".format(count / float(data[0]) * 100))

