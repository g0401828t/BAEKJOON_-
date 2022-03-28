## Solution
import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
data_set = list(set(data))
data_set.sort()

dic = {data_set[i] : i for i in range(len(data_set))}
# print(dic)
# print(data)
for i in data:
    print(dic[i], end=" ")

## 풀이 3 ==> 시간초과..
import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
data_set = list(set(data))
data_set.sort()

for i in range(N):
    print(data_set.index(data[i]), end=" ")


## 풀이 2 ==> 시간초과...
import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data_set = list(set(data))
data_set.sort()

new_data = []
for i in range(N):
    new_data.append(data_set.index(data[i]))
print(*new_data)


## 풀이 1 ==> 시간초과...
import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data_set = list(set(data))

new_data = []
for n in range(N):
    xi = data[n]
    new_xi = 0
    for i in range(len(data_set)):
        if xi > data_set[i]:
            new_xi += 1
    new_data.append(new_xi)
print(*new_data)

