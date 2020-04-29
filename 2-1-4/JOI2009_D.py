from itertools import permutations

N = int(input())
K = int(input())
C = [input() for _ in range(N)]

s = set()
for p in permutations(C, K):
    s.add(''.join(p))

print(len(s))