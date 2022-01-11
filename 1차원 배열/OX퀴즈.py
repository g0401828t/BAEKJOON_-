import sys

N = int(input())

for n in range(N):
    data = list(map(str, sys.stdin.readline().rstrip()))

    prev = "n"
    result = 0
    point = 0
    for d in data:
        if d == "O":
            point += 1
        else:
            point = 0
        
        result += point
    
    print(result)
        
# # 2nd trial
# import sys

# N = int(input())

# for n in range(N):
#     data = list(map(str, sys.stdin.readline().rstrip()))

#     result = 0
#     point = 0
#     for d in data:
#         if d == "O":
#             point += 1
#         else:
#             point = 0
        
#         result += point
    
#     print(result)
        


