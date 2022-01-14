# # 혼자 풀이
# import sys

# data = sys.stdin.readline()

# count = 1
# before = data[0]
# dz = False
# for i in range(1, len(data)-1):
#     d = data[i]
#     if before == "c" and (d == "=" or d == "-"):            # c=, c-
#         before = d  
#         dz = False
#         continue
#     elif before == "d" and d == "z":                        # dz=
#         before = d  
#         dz = True
#         count += 1
#         continue
#     elif dz == True:
#         if d == "=":
#             count -= 1
#             before = d
#             dz = False
#             continue
#         else:
#             count += 1
#             before = d
#             dz = False
#             continue
#     elif before == "d" and d == "-":                        # d-
#         before = d  
#         dz = False
#         continue
#     elif (before == "l" or before == "n") and d == "j":    # lj, nj
#         before = d  
#         dz = False
#         continue
#     elif (before == "s" or before == "z") and (d == "="):  # s=, z=
#         before = d  
#         dz = False
#         continue
#     else:
#         count += 1
#         before = d
#         dz = False

# print(count)

# # 정석 => replace를 통해 문자여 변환 할 수 있다.
import sys

data = sys.stdin.readline().strip()     # 개행 문자 없이
# data = input()                        # 원래 개행 문자 없ㅇ 받음

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
    data = data.replace(i, "*")

print(len(data))
