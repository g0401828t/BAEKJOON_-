import sys

A, B, V = map(int, sys.stdin.readline().split())

# # time error
# total = 0
# day = 1
# while True:
#     total += A
#     if total >= V:
#         print(day)
#         break
#     day += 1
#     total -= B

# # 2nd Trial 실패
# one_day = A-B
# days = V // one_day
# if V % one_day != 0:
#     days += 1
# else:
#     V -= A
#     days = V // one_day + 1

# print(days)

# # 3rd Trial  성공
# (A - B) * (n-1) + A >= V   => n 번째날 성공
# n >= (V-A) / (A-B) + 1

n = (V-A) / (A-B) + 1
if (V-A) % (A-B) != 0:
    print(int(n)+1)
else:
    print(int(n))
