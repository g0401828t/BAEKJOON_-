import sys

T = int(sys.stdin.readline())
for i in range(T):
    R, S = map(str, sys.stdin.readline().split())

    P = ""
    for s in S:
        P += s * int(R)
    print(P)
