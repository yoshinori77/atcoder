from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
C = list(list(input()) for i in range(R))
q = deque([[sy-1, sx-1]])
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
C[sy-1][sx-1] = 0

while q:
    y, x = q.popleft()
    for dy, dx in d:
        if C[y+dy][x+dx] == ".":
            C[y+dy][x+dx] = C[y][x]+1
            q.append([y+dy, x+dx])
print(C[gy-1][gx-1])


# import sys


# H, W = map(int, input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
# import ipdb; ipdb.set_trace()
# C = [list(input()) for _ in range(H)]
# C[gy-1][gx-1] = 'g'
# min_cnt = 10**10

# # 再帰による実装
# sys.setrecursionlimit(10 ** 7)


# def dfs(y, x):
#     global min_cnt
#     cnt = 0
#     if not (0 <= y < H) or not (0 <= x < W) or C[y][x] == '#':
#         return
#     if C[y][x] == 'g':
#         min_cnt = min(min_cnt, cnt)
#         exit()
#     C[y][x] = '#'  # 探索済み
#     cnt += 1
#     dfs(y + 1, x)
#     dfs(y - 1, x)
#     dfs(y, x + 1)
#     dfs(y, x - 1)

# dfs(sy, sx)
# print(min_cnt)
