from operator import itemgetter

N = int(input())
R = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]
R = sorted(R, key=itemgetter(1), reverse=True)
B = sorted(B, key=itemgetter(0))

count = 0
for c, d in B:
    for a, b in R:
        if (a < c) & (b < d):
            count += 1
            R.remove((a, b))
            break
print(count)
