# # 1st Sol   2021.08.xx
N = int(input())

count = 0
for n in range(1, N+1):
  n_str = str(n)
  # print("=====", n_str)

  # 1, 2자리 수
  if len(n_str) == 1 or len(n_str) == 2:
    count += 1
  # 3자리 수 이상
  else:
    # 앞 뒤 자리 수 차이 구하면서 확인
    b_diff = int(n_str[1]) - int(n_str[0])
    # print(b_diff)
    for i in range(len(n_str)):

      if i == len(n_str)-1:
        # print("마지막 자리!")
        count += 1
        break
      
      diff = int(n_str[i+1]) - int(n_str[i])
      if diff != b_diff:
        break
        

      # print("diff:", diff)

print(count)



# # # 2nd Sol   2022.01.12
# def Han(X):
#     X = str(X)
#     prev = int(X[0])
#     next = int(X[1])
#     pre_diff = next - prev
#     for i in range(1, len(X)-1):
#         prev, next = int(X[i]), int(X[i+1])
#         diff = next - prev

#         if pre_diff == diff:
#             pre_diff = diff
#         else:
#             return False
    
#     return True


# N = int(input())


# count = 0
# for n in range(1, N+1):
#     if n < 100:
#         count += 1
#     else:
#         if Han(n):
#             count += 1

# print(count)

