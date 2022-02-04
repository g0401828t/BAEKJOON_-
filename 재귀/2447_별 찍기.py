import sys 

# sys.setrecursionlimit(10**6) 

def append_star(N): 
    # N == 3
    if N == 3: 
        return ['***', '* *', '***'] 
        
    Stars = append_star(N//3) 
    
    # N > 3
    L = [] 
    for S in Stars: 
        L.append(S*3) 
    for S in Stars: 
        L.append(S+' '*(N//3)+S) 
    for S in Stars: 
        L.append(S*3) 
    return L 
    
n = int(sys.stdin.readline().strip()) 

for x in append_star(n):
    print(x)
