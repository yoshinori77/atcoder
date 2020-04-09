from itertools import combinations
import math

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]

max_distance = 0
for a, b in combinations(L, 2):
  distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
  max_distance = max(max_distance, distance)

print('{:.6f}'.format(max_distance))