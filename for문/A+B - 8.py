import sys

for n in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(n+1, A, B, A+B))

