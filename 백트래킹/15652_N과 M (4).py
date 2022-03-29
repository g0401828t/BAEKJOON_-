import sys

## 풀이 1: DFS로 풀기
N, M = map(int, sys.stdin.readline().split())
s = []

def dfs(start, N, M):
    if len(s) == M:
        print(*s)
        return
    
    for i in range(start, N+1):
        s.append(i)
        dfs(i, N, M)
        s.pop()

dfs(1, N, M)

## 풀이 2: 중복 순열로 풀기
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())

for i in combinations_with_replacement([i+1 for i in range(N)], M):
    print(*i)
