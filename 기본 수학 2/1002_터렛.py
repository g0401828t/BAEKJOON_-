import sys

N = int(sys.stdin.readline())
"""
# 3rd Trial => 두 원이 한점에서 만나는지 두점에서 만나는지 아니면 안 만나는지 확인하고 아예 겹치면 무한대다!!!!!
# 여러가지 경우의 수 생각해야함
"""
for n in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if distance > r1+r2:
        print(0)
    elif distance == r1+r2:
        print(1)
    elif distance > 0 and distance < r1+r2: # 두점에서 만나는 경우와 작은 원이 큰원 안에서 한점에서 만나는 경우!
        if distance + min([r1, r2]) == max([r1, r2]):
            print(1)
        elif distance + min([r1, r2]) < max([r1, r2]):
            print(0)
        else:
            print(2)
    else: # distance == 0
        if r1 == r2:
            print(-1)
        else:
            print(0)
