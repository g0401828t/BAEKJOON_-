import sys

N = 1
for i in range(3):
    N *= int(sys.stdin.readline())

N = str(N)
data = []
for n in N:
    data.append(int(n))

for i in range(10):
    count = 0
    for d in data:
        if d == i:
            count += 1
    print(count)

# # #  2nd sol
# import sys

# N = 1
# for i in range(3):
#     N *= int(sys.stdin.readline())

# N = str(N)
# data = []
# for n in N:
#     data.append(int(n))

# for i in range(10):
#     print(data.count(i))
