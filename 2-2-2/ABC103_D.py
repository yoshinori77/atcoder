import sys
from operator import itemgetter
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]
ab.sort(key=itemgetter(1))
east_island = ab[0][1]
answer = 1

for i, j in ab:
    if i >= east_island:
        answer += 1
        east_island = j

print(answer)
