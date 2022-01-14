import sys

def Group(data):
    prev = data[0]
    new_data = prev
    for i in range(1, len(data)):
        d = data[i]
        if d != prev:
            new_data += d
            prev = d
    
    if len(new_data) == len(list(set(data))):
        return True
    else:
        False

N = int(sys.stdin.readline())

count = 0
for n in range(N):
    data = sys.stdin.readline().strip()

    if Group(data) == True:
        count += 1

print(count)    
