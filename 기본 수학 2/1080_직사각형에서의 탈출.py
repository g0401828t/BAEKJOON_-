import sys

x, y, w, h = map(int, sys.stdin.readline().split())

left, down = x, y
right, up = w-x, h-y

print(min([left, down, right, up]))
