a = [list(input()) for _ in range(10)]
visited = [['x' for _ in range(10)] for _ in range(10)]


def dfs(y, x):
    if y < 0 or y >= 10 or x < 0 or x >= 10:
        return
    if a[y][x] == 'x':
        return
    if visited[y][x] == 'o':
        return

    visited[y][x] = 'o'

    dfs(y+1, x)
    dfs(y-1, x)
    dfs(y, x+1)
    dfs(y, x-1)


flag = False
for y in range(10):
    for x in range(10):
        if a[y][x] == 'x':
            visited = [['x' for _ in range(10)] for _ in range(10)]
            a[y][x] = 'o'
            dfs(y, x)
            if a == visited:
                flag = True
                break
            a[y][x] = 'x'
    if flag:
        break

if flag:
    print('YES')
else:
    print('NO')
