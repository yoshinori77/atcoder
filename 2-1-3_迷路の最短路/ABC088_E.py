from collections import deque

H, W = map(int, input().split())
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
            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj] and C[ni][nj] != '#':
                visited[ni][nj] = True
                que.append((ni, nj, c+1))
    return 0


sg = [[0, 0], [H-1, W-1]]
ans = 0
ans += bfs(sg[0], sg[1])

if ans == 0:
    print('-1')
else:
    num = sum([n.count('#') for n in C])
    result = H * W - (num + ans + 1)
    print(result)
