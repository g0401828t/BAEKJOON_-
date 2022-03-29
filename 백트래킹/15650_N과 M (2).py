n,m = list(map(int,input().split()))
 
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

