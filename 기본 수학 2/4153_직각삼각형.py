import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a==0 and b==0 and c==0:
        break
    else:
        long_line = max([a, b, c])
        x_and_y = [a, b, c]
        x_and_y.remove(long_line)
        x, y = x_and_y

        if long_line**2 == (x ** 2 + y ** 2):
            print("right")
        else:
            print("wrong")
