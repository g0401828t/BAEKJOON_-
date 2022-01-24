# # 1st Trial => 시가 초과
import sys

def sosu(X):
  if X == 1:
    return False
  elif X == 2:
    return True
  else:
    for x in range(2, int(X/2) + 1):
      if X % x == 0:
        return False
    return True

while True:
  n = int(sys.stdin.readline())

  if n == 0:
    break

  count = 0
  for n in range(n+1, 2*n+1):
    if sosu(n):
      count += 1
  print(count)

# # 1st Sol:
import sys

def howmany_sosu(X):
  # [X+1, X+2, ... , 2X]
  # [2, 3, 4, 5, ..., 2X]
  data = [True] * (2*X - 1)

  for x in range(2, 2*X + 1):
    if data[x-2] == True:
      for i in range(2*x, 2*X + 1, x):
        # print("i:", i)
        data[i-2] = False
        # print(data) 
  
  count = 0
  for d in range(X-1, len(data)):
    if data[d] == True:
      count += 1  
  return count

while True:
  n = int(sys.stdin.readline())

  if n == 0:
    break
  if n == 1:
    print(1)
  else:
    result = howmany_sosu(n)
    print(result)
