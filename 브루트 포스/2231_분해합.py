import sys

# abc => abc+a+b+c = 101a + 11b + 1c

N = int(sys.stdin.readline())

have = False
out = []
for n in range(1, N):
    total = n

    for i in str(n):
        total += int(i)
    
    if total == N:
        print(n)
        # out.append(n)
        have = True
        break

# if have == True:
#     print(out)
if have == False:
    print(0)
