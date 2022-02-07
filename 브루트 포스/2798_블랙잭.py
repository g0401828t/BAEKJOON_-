import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
kards = list(map(int, sys.stdin.readline().split()))

kards_permutations = itertools.permutations(kards, 3)

best = 0
for three_kards in kards_permutations:
    if sum(three_kards) <= M:
        if best < sum(three_kards):
            best = sum(three_kards)

print(best)
