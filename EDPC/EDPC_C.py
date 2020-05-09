N = int(input())

A, B, C = 0, 0, 0
for _ in range(N):
    a, b, c = map(int, input().split())
    A, B, C = max(B, C) + a, max(C, A) + b, max(A, B) + c
ans = max(A, B, C)

print(ans)