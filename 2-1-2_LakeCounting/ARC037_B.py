def dfs(v, p):
    global closed_path

    seen[v] = True
    for next_v in g[v]:
        if next_v == p:
            continue
        if seen[next_v]:
            closed_path = True
            continue
        dfs(next_v, v)


N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
seen = {i: False for i in range(N+1)}
for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


cnt = 0
for v in range(1, N+1):
    if seen[v]:
        continue
    closed_path = False
    dfs(v, 0)
    if not closed_path:
        cnt += 1

print(cnt)
