import sys

N = int(sys.stdin.readline())
for n in range(N, 0, -1):
    print(" "*(n-1) + "*"*(N - n + 1))

