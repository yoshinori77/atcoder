N = int(input())
W = [int(input()) for _ in range(N)]
D = [W[0]]

for i in range(1, N):
    b = W[i]
    if max(D) < b:
        D.append(b)
    else:
        for j in range(len(D)):
            if D[j] >= b:
                D[j] = b
                break

print(len(D))