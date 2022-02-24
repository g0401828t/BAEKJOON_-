import sys

Num = str(sys.stdin.readline().strip())

data = []
for n in Num:
    data.append(int(n))

data.sort(reverse=True)

result = ''
for d in data:
    result = result + str(d)
print(result)
