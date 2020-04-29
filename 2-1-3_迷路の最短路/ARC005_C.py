from collections import deque

H, W = map(int, input().split())
C = [input() for i in range(H)]
dst = [[3]*W for j in range(H)]


def bfs(mtrx, dst, sy, sx):
	queue = deque([[sy, sx]])
	dst[sy][sx] = 0
	while queue:
		y, x = queue.popleft()
		for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
			ny, nx = y+j, x+k
			if (0 <= nx < W and 0 <= ny < H):
				if dst[ny][nx] != 3:
					continue
				if mtrx[ny][nx] == 'g':
					return "YES"
				if mtrx[ny][nx] == '#':
					if dst[y][x] < 2:
						queue.append([ny, nx])
						dst[ny][nx] = dst[y][x] + 1
				else:
					queue.appendleft([ny, nx])
					dst[ny][nx] = dst[y][x]
	return "NO"


for i in range(H):
	for j in range(W):
		if C[i][j] == "s":
			sy, sx = i, j

print(bfs(C, dst, sy, sx))
