import sys
N = int(sys.stdin.readline())


for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())

    diff = B - A

    i = 1
    total = 0
    while True:
        n = 2*i
        total += n

        if total >= diff:
            back = total - diff
            if back > i-1:
                print(n-1)
                break
            else:
                print(n)
                break
        
        i += 1
