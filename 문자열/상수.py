import sys

A, B = map(str, sys.stdin.readline().split())



a, b = "", ""
for i in range(3):
    a += A[2 - i]
    b += B[2 - i]

print(max([a, b]))
