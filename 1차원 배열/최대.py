import sys


data = []
index = 0
while True:
    try:
        data.append(int(sys.stdin.readline()))
    except:
        break

max = max(data)
print(max)


for d in data:
    index += 1
    if d == max:
        print(index)
        
# # 2nd sol
# import sys


# data = []
# index = 0
# while True:
#     try:
#         data.append(int(sys.stdin.readline()))
#     except:
#         break

# max = max(data)
# print(max)


# print(data.index(max) + 1)
