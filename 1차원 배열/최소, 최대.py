import sys

N = int(sys.stdin.readline())

Data = list(map(int, sys.stdin.readline().split()))


for i, d in enumerate(Data):
    if i == 0:
        l, L = d, d
    else:
        if d < l:
            l = d
        elif d > L:
            L = d
    
print(l, L)


