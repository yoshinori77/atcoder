from collections import deque
H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
C = list(list(input()) for i in range(H))
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
