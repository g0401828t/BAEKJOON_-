# # 1st Trial => 시간 초과
# import math
# import sys
# from itertools import product

# def Sosu_list(X):
#   data = [True] * X
#   sosu_list = []
#   for x in range(1, int(X**0.5)+1):
#     if x == 1:
#       data[x-1] = False
#     elif data[x-1] == True:
#       for i in range(2*x, X+1, x):
#         data[i-1] = False
  
#   for d in range(len(data)):
#     if data[d] == True:
#       sosu_list.append(d+1)

#   return sosu_list

# T = int(sys.stdin.readline())

# for t in range(T):
#   n = int(sys.stdin.readline())

#   sosu_list = Sosu_list(n)
#   print(sosu_list)
  
#   diff = math.inf
#   for s in sosu_list:
#     for o in sosu_list:
#       if s+o == n and abs(s-o) < diff:
#         result1, result2 = s, o
#         diff = abs(s-o)

#   # # 중복 순열도 시간 초과....
#   # diff = math.inf
#   # for i in product(sosu_list, sosu_list):
#   #   if sum(i) == n and abs(i[0] - i[1]) < diff:
#   #     result1, result2 = i[0], i[1]
#   #     diff = abs(i[0] - i[1]) 

#   print(result1, result2)

# # 2nd Trial: sosu list 찾으면서 바로 구하기 => 시간초과
# import math
# import sys
# from itertools import product

# def Sosu_list(X):
#   data = [True] * X
#   sosu_list = []
#   for x in range(1, int(X**0.5)+1):
#     if x == 1:
#       data[x-1] = False
#     elif data[x-1] == True:
#       for i in range(2*x, X+1, x):
#         data[i-1] = False
  
#   diff = math.inf
#   for d in range(len(data)):
#     for b in range(len(data)):
#       if data[d] == True and data[b] == True:
#         # print(d+1, b+1)
#         if (d+1) + (b+1) == X and abs((d+1) - (b+1)) < diff:
#           result1, result2 = d+1, b+1
#           diff = abs((d+1) - (b+1))

#   return result1, result2

# T = int(sys.stdin.readline())

# for t in range(T):
#   n = int(sys.stdin.readline())

#   result1, result2 = Sosu_list(n)

#   print(result1, result2)


# # 3rd Trial => .remove()를 통해 소수 찾는 부분 시간 단축 시도 했지만 실패... => 시간 초과
# import math
# import sys
# from itertools import product

# def Sosu_list(X):
#   sosu_list = [i for i in range(2, X+1)]

#   for s in sosu_list:
#     for i in range(s*2, X+1, s):
#       try:
#         sosu_list.remove(i)
#       except:
#         continue

#   return sosu_list



# T = int(sys.stdin.readline())

# for t in range(T):
#   n = int(sys.stdin.readline())

#   sosu_list = Sosu_list(n)
#   # print(sosu_list)
  
#   diff = math.inf
#   for s in sosu_list:
#     for o in sosu_list:
#       if s+o == n and abs(s-o) < diff:
#         result1, result2 = s, o
#         diff = abs(s-o)

#   print(result1, result2)

# # 4th Trial => 미리 제한된 n보다 작은 수들의 소수 리스트 만들어 놓고 진행 => 시간 초과...
import math
import sys
from itertools import product

def make_Sosu_list():
  sosu_list = [i for i in range(2, 10001)]

  for s in sosu_list:
    for i in range(s*2, 10001, s):
      try:
        sosu_list.remove(i)
      except:
        continue

  return sosu_list



sosu_list = make_Sosu_list()
print(sosu_list)
  
T = int(sys.stdin.readline())

for t in range(T):
  n = int(sys.stdin.readline())

  diff = math.inf
  for s in sosu_list:
    if s>n:
        break
    for o in sosu_list:
      if o>n:
        break
      if s+o == n and abs(s-o) < diff:
        result1, result2 = s, o
        diff = abs(s-o)
          

  print(result1, result2)





