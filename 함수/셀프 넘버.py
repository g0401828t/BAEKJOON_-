# # 1st trail -> 시간초과
# def solve():
#     for i in range(1, 10001):
        
#         thereis = 0
#         for a in range(10):
#             for b in range(10):
#                 for c in range(10):
#                     for d in range(10):
#                         d = 1001*d + 101*c + 11*b + 2*a

#                         if d == i:
#                             thereis = 1
#                     if thereis == 1:
#                         break
#                 if thereis == 1:
#                     break
#             if thereis == 1:
#                 break
        
#         if thereis == 0:
#             print(i)

# 1st Sol
def D(n):
    N = str(n)

    result = n
    for i in N:
        result += int(i)
    
    return result

not_self = set()
for i in range(1, 10001):
    not_self.add(D(i))

all = set([n for n in range(1, 10001)])

for i in sorted(all - not_self):
    print(i)
