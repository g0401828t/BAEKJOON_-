import sys

def FindSosu(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True




M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

result = 0
for n in range(M, N+1):
    if FindSosu(n):
        if result == 0:
            first_sosu = n
        result += n


if result != 0:
    print(result)
    print(first_sosu)
else:
    print(-1)
