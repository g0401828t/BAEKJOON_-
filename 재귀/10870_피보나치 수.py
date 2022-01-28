import sys

N = int(sys.stdin.readline())

def fibonacci(X):
    if X==0:
        return 0
    elif X==1:    
        return 1
    else:
        return fibonacci(X-1) + fibonacci(X-2)

print(fibonacci(N))
