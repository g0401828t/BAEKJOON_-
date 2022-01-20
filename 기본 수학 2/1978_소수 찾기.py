import sys

N = int(sys.stdin.readline())

data = map(int, sys.stdin.readline().split())

count = 0
for d in data:
    sosu = True
    for i in range(2, d):
        if d % i == 0:
            sosu = False
    if d != 1 and sosu == True:
        count += 1
print(count)
