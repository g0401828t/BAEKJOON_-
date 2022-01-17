import sys

T = int(sys.stdin.readline())
for t in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    YY = N % H
    XX = N // H + 1
    if YY == 0:     # 꼭대기 층일 때
        YY = H
        XX -= 1

    if XX < 10:
        XX = str(0) + str(XX)
    print(str(YY) + str(XX))


