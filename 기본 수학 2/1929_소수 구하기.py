# # 1st Trial => 시간 초과
import sys

def IsSosu(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True



M, N = map(int, sys.stdin.readline().split())

for n in range(M, N+1):
    if IsSosu(n):
        print(n)

# # 2nd Trial ==> 시가 초과...
import sys

def IsSosu(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True



M, N = map(int, sys.stdin.readline().split())

sosu = [2]
for n in range(2, M):
    if IsSosu(n):
        sosu.append(n)

if M == 1: 
    M += 1
for m in range(M, N+1):
    if m == 2:
        print(m)
    is_sosu = True
    for s in sosu:
        if m % s == 0:
            is_sosu = False
    if is_sosu:
        print(m)
        sosu.append(m)

