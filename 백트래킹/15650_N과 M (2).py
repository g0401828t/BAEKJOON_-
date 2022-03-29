## 풀이 1: DFS로 풀기
,m = list(map(int,input().split()))
 
s = []
visited = [False] * n
 
def dfs(start, n, m):
    if len(s)==m:
        print(*s)
        return
    
    for i in range(start, len(visited)):
        if visited[i] == False:
            s.append(i+1)
            visited[i] = True
            dfs(i, n, m)
            s.pop()
            visited[i] = False
 
dfs(0, n, m)

## 풀이 2: 조합으로 풀기
import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

comb = combinations(range(1, N+1), M)
for i in comb:
    print(*i)
