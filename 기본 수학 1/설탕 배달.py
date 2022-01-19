# # # 1st Sol
# import math

# N = int(input())

# result = math.inf
# total = 0
# for i in range(N//5 + 1):
#     remain = N - (5*i)
#     total += i
#     while remain > 0:
#         remain -= 3
#         total += 1
    
#     if result >= total and remain == 0:
#         result = total
#     total = 0

# if result == math.inf:
#     print(-1)
# else:
#     print(result)
    
# # 2nd Sol
N = int(input())

result = 0
while N>=0:
    if N % 5 ==0:
        result += N//5
        print(result)
        break
    
    N -= 3
    result += 1
else:
    print(-1)
