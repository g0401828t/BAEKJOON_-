# # 1st ans
# N = str(input())
# N_new = N
# result = 0
# while True:
#     result += 1
#     if len(N_new) == 2:
#         a, b = int(N_new[0]), int(N_new[1])
#     else:
#         a, b = 0, int(N_new[0])

#     if len(str(a+b)) == 2:
#         N_new = str(b) + str(a+b)[1]
#     else:
#         N_new = str(b) + str(a+b)

#     if int(N) == int(N_new):
#         print(result)
#         break
    
#     if result == 60:
#         break

# # 2nd ans
# N = str(input())
# N_new = N
# result = 0
# while True:
#     result += 1
#     if len(N_new) == 2:
#         a, b = int(N_new[0]), int(N_new[1])
#     else:
#         a, b = 0, int(N_new[0])

#     if len(str(a+b)) == 2:
#         N_new = str(b) + str(a+b)[1]
#     else:
#         N_new = str(b) + str(a+b)

#     if int(N) == int(N_new):
#         print(result)
#         break
    
# # 3rd ans
N = int(input())
N_new = -1
result = 0
while N_new != N:
    result += 1
    
    if N_new == -1:
        N_new = N
    N_new = (N_new%10)*10 + (N_new//10 + N_new%10)%10
    

print(result)    

