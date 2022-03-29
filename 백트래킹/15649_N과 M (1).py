## 풀이 1: DFS로 풀기
n,m = list(map(int,input().split()))
 
s = []
visited = [False] * n
 
def dfs():
    if len(s)==m:
        print(*s)
        return
    
    for i in range(len(visited)):
        if visited[i] == False:
            s.append(i+1)
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False
 
dfs()

## 풀이 2: 순열로 풀기
import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

for i in permutations([i+1 for i in range(N)], M):
    print(*i)
