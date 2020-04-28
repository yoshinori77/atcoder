import numpy as np

H, W = map(int, input().split())
grid = (np.array([list(input())
                  for _ in range(H)]) == "#")
cost = np.full((H, W), 10 ** 9, dtype=np.int64)
cost[grid[:, :]] = 0

for i in range(1, H):
    cost[i] = np.minimum(cost[i], cost[i - 1] + 1)

for i in range(H - 2, -1, -1):
    cost[i] = np.minimum(cost[i], cost[i + 1] + 1)

for i in range(1, W):
    cost[:, i] = np.minimum(cost[:, i], cost[:, i - 1] + 1)

for i in range(W - 2, -1, -1):
    cost[:, i] = np.minimum(cost[:, i], cost[:, i + 1] + 1)

print(np.max(cost))
