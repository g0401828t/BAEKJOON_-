import sys

N = int(sys.stdin.readline())

count = [0 for _ in range(10001)]
for _ in range(N):
    n = int(sys.stdin.readline())
    count[n] += 1

for i in range(len(count)):
    # if count[i] > 0:    # 불필요한 연산 줄이자
    for _ in range(count[i]):
        print(i)
