h, min = map(int, input().split())

if min < 45:
    min = 60 - (45 - min)
    if h == 0:
        h = 23
    else:
        h -= 1
else:
    min -= 45

print(h, min)
