import sys

N = int(sys.stdin.readline())

weight, height = [], []
for n in range(N):
    w, h = map(int, sys.stdin.readline().split())

    weight.append(w)
    height.append(h)

result = []
for i in range(N):
    rank = 1
    for j in range(N):
        my_weight, my_height = weight[i], height[i]
        friends_weight, friends_height = weight[j], height[j]

        if my_weight < friends_weight and my_height < friends_height :
            rank += 1

    result.append(rank)

# print(result)
for i in result:
    print(i, end=" ")
