from collections import deque

H, W, N = map(int, input().split())
C = [input() for _ in range(H)]

move = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(S, G):

    visited = [[False] * W for _ in range(H)]
    c = 0

    visited[S[0]][S[1]] = True
    que = deque([(S[0], S[1], 0)])

    while que:
        ci, cj, c = que.popleft()

        if ci == G[0] and cj == G[1]:
            return c

        for di, dj in move:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and C[ni][nj] != 'X':
                visited[ni][nj] = True
                que.append((ni, nj, c+1))


sg = [[-1, -1] for i in range(N+1)]

for i in range(H):
    for j in range(W):
        if C[i][j] == 'S':
            sg[0] = [i, j]
        elif C[i][j] in '123456789':
            sg[int(C[i][j])] = [i, j]

ans = 0
for i in range(N):
    ans += bfs(sg[i], sg[i+1])

print(ans)
