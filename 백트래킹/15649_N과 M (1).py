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

