import sys

N = int(sys.stdin.readline())

def factorial(X):
    if X == 1 or X == 0 :
        return 1
    else:
        return factorial(X-1) * X

print(factorial(N))
