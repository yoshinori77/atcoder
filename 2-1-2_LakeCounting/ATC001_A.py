import sys

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

# 再帰による実装
sys.setrecursionlimit(10 ** 7)


def dfs(x, y):
	if not (0 <= x < H) or not (0 <= y < W) or C[x][y] == '#':
		return 0
	if C[x][y] == 'g':
		print('Yes')
		exit()
	C[x][y] = '#'  # 探索済み
	dfs(x + 1, y)
	dfs(x - 1, y)
	dfs(x, y + 1)
	dfs(x, y - 1)


def start_point(H, W):
    for i in range(H):
        for j in range(W):
            if C[i][j] == 's':
                return i, j  # start point


sx, sy = start_point(H, W)
dfs(sx, sy)
print('No')
