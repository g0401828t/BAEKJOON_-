import sys

T = sys.stdin.readline()

# 모든 소문자를 대문자로 먼저 바꾼다
data = []
for i in range(len(T) - 1):     # 마지막 개행("\n") 없애기 위해 -1 번째까지만 받음
    t = T[i]
    if ord(t) >= 97 and ord(t) <=122:
        t = chr(ord(t) - 32)
    data.append(t)


# 문자들의 종류만 모아놓음
set_T = set(data)

best = 0
for t in set_T:
    num = data.count(t)
    
    if num == best:
        result = "?"
        
    if num > best:
        best = num
        result = t

print(result)
