import sys

A, B, C = map(int, sys.stdin.readline().split())

# 총 비용 A + nB 
# 총 수입 nC


# n = A / (C-B)
# if n<0:  # C=B 일때 zero division error가 뜬다.
if B>=C:
    print(-1)
else:
    n = A / (C-B)
    print(int(n) + 1)
