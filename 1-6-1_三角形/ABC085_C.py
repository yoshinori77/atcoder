N, Y = map(int, input().split())

count = 0
x, y, z = -1, -1, -1
for i in range(N+1):
  for j in range(N+1):
    if i + j > N:
      continue
    if Y - (10000*i + 5000*j) == 1000*(N - i - j):
      x, y, z = i, j, (N - i -j)
      break

print(x, y, z)