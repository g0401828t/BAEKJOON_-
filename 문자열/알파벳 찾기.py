N = list(map(str, input().strip()))

alphabets = [-1 for _ in range(26)]
for i, n in enumerate(N):
    index = ord(n) - ord("a")
    if alphabets[index] == -1:
        alphabets[index] = i

for i in alphabets:
    print(i, end=' ')


