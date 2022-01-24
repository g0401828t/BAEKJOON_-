# # # 1st Trial => 시간 초과
# import sys

# def IsSosu(x):
#     if x == 1:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True



# M, N = map(int, sys.stdin.readline().split())

# for n in range(M, N+1):
#     if IsSosu(n):
#         print(n)

# # # 2nd Trial ==> 시가 초과...
# import sys

# def IsSosu(x):
#     if x == 1:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# # # 2nd Trial => 시간 초과
# M, N = map(int, sys.stdin.readline().split())

# sosu = [2]
# for n in range(2, M):
#     if IsSosu(n):
#         sosu.append(n)

# if M == 1: 
#     M += 1
# for m in range(M, N+1):
#     if m == 2:
#         print(m)
#     is_sosu = True
#     for s in sosu:
#         if m % s == 0:
#             is_sosu = False
#     if is_sosu:
#         print(m)
#         sosu.append(m)

        
# # 1st Sol => 1~X 까지가 아닌 X으 제곱근 까지만 검사하면 된다.        
import sys

M, N = map(int, sys.stdin.readline().split())

def sosu(X):
    if X == 1:
        return False
    else:
        for x in (2, int(X**0.5) + 1):
            if X % x == 0:
                return False
        return True

for i in range(M, N+1):
    if sosu(i):
        print(i)

        
# # 2nd Sol => 에라토스테네스의 체
m, n = map(int, input().split())

def isprime(m, n):
  n += 1
  prime = [True] * n                # n개의 [True]가 있는 리스트 생성
  for i in range(2, n):
    if prime[i]:                    # prime[i]가 True일때
      for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
        prime[j] = False

  for i in range(m, n):
    if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
      print(i)

isprime(m, n)
