import sys

N = int(sys.stdin.readline().strip())

data = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x, y))

# print(sorted(data, key=lambda x: (x[0], x[1])))
result_data = sorted(data, key=lambda x: (x[0], x[1]))
for result in result_data:
    print(result[0], result[1])
