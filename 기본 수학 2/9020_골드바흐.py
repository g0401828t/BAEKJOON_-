# # 1st Trial => 시간 초과
import math
import sys
from itertools import product

def Sosu_list(X):
  data = [True] * X
  sosu_list = []
  for x in range(1, int(X**0.5)+1):
    if x == 1:
      data[x-1] = False
    elif data[x-1] == True:
      for i in range(2*x, X+1, x):
        data[i-1] = False
  
  for d in range(len(data)):
    if data[d] == True:
      sosu_list.append(d+1)

  return sosu_list

T = int(sys.stdin.readline())

for t in range(T):
  n = int(sys.stdin.readline())

  sosu_list = Sosu_list(n)
  print(sosu_list)
  
  diff = math.inf
  for s in sosu_list:
    for o in sosu_list:
      if s+o == n and abs(s-o) < diff:
        result1, result2 = s, o
        diff = abs(s-o)

  # # 중복 순열도 시간 초과....
  # diff = math.inf
  # for i in product(sosu_list, sosu_list):
  #   if sum(i) == n and abs(i[0] - i[1]) < diff:
  #     result1, result2 = i[0], i[1]
  #     diff = abs(i[0] - i[1]) 

  print(result1, result2)
