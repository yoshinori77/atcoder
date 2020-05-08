import numpy as np

N, W = map(int, input().split())
s = np.full(N * 1000 + 1, W + 1)
s[0] = 0
for i in range(N):
    w, v = map(int, input().split())
    s[v:] = np.minimum(s[v:], s[:-v] + w)
print(np.max(np.where(s <= W)))
