N = int(input())
robots = [tuple(map(int, input().split())) for _ in range(N)]
robots = [(x+l, x-l) for x, l in robots]
robots.sort()

cnt = 0
last = -float('inf')
for right, left in robots:
    # 手前のロボットの右手が次のロボットの左手よりも小さいか判定
    if last <= left:
        cnt += 1
        last = right

print(cnt)
