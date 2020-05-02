import bisect

N = int(input())
T = [tuple(map(int, input().split())) for i in range(N)]
T = sorted(T, key=lambda x: (x[0], -x[1]))

L = [0]
for a, b in T:
    if b > L[-1]:
        L.append(b)
    else:
        j = bisect.bisect_left(L, b)
        L[j] = b

print(len(L) - 1)
