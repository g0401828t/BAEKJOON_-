import sys

N = int(sys.stdin.readline())

i = 666
count = 0
while True:
    if '666' in str(i):
        count += 1
    
    if count == N:
        break

    i += 1

print(i)
