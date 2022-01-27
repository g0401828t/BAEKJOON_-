import sys

# # 1st Sol
xs, ys = [0]*1001, [0]*1001
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xs[x] += 1
    ys[y] += 1

print(xs.index(1), ys.index(1))

# # 2nd Sol
xs, ys = [], []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xs.append(x)
    ys.append(y)
for i in range(3):
    if xs.count(xs[i]) == 1:
        result_x = xs[i]
    if ys.count(ys[i]) == 1:
        result_y = ys[i]
print(result_x, result_y)
