import sys

N = int(sys.stdin.readline())

count = [0 for _ in range(4000 + 1 + 4000)]
for _ in range(N):
    n = int(sys.stdin.readline())
    count[n + 4000] += 1

result1 = 0
middle = N // 2
middle_count = 0
max_count = max(count)
max_count_count = 0
first = False
last = False
for i in range(len(count)):
    if count[i] == max_count and max_count_count < 2:
        max_count_count += 1
        result3 = i - 4000

    for _ in range(count[i]):
        result1 += (i - 4000)
        if middle_count == N //2:
            result2 = i - 4000
        middle_count += 1
        
        if not first:
            first_num = i - 4000
            first = True
        last_num = i - 4000

print(round(result1 / N))
print(result2)
print(result3)
print(last_num - first_num)
