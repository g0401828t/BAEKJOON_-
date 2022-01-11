import sys

data = []
for i in range(10):
    data.append(int(sys.stdin.readline()) % 42)

count = 0
for i in range(42):
    if data.count(i) != 0:
        count += 1

print(count)




# # 2nd trial

# import sys

# data = []
# for i in range(10):
#     data.append(int(sys.stdin.readline()) % 42)

# data = set(data)


# print(len(data))
