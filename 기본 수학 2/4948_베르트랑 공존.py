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

