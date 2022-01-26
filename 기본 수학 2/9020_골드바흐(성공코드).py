"""
결과 값의 패턴을 잘 보아라...
n의 중간값이 소수이면 정담
아니면 정답인 소수 두개는 n의 중간값으로부터 같은 거리만큼 위치한 소수이다...!!!! (이게 중요한 포인트!!)
따라서 중간부터 검사해나가면 무조건 소수의 차이가 가장 적다!!
"""
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
  # print(sosu_list)
  
  if n/2 in sosu_list:
    print(n//2, n//2)
  else:
    diff = math.inf
    result1, result2 = n/2, n/2
    while True:
      result1 -= 1
      result2 += 1
      if result1 in sosu_list:
        if result2 in sosu_list:
          print(int(result1), int(result2))
          break





