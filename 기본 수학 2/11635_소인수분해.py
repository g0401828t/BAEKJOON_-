import sys


N = int(sys.stdin.readline())

for n in range(2, N+1):
    while N % n == 0:
        N /= n
        print(n)

