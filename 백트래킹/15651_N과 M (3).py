import sys

## 풀이 1: DFS로 풀기
N, M = map(int, sys.stdin.readline().split())
s = []

def dfs():
    if len(s) == M:
        print(*s)
        return
    
    for i in range(1, N+1):
        s.append(i)
        dfs()
        s.pop()

dfs()

## 풀이 2: 중복 순열로 풀기
# from itertools import product

# N, M = map(int, sys.stdin.readline().split())

# for i in product([i+1 for i in range(N)], repeat=M):
#     print(*i)
