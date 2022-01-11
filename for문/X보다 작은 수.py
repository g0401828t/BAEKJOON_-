import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

new_A = []
for a in A:
    if a < X:
        print(a, end=" ")

