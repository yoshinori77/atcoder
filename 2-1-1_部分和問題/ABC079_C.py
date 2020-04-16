N = 4
A = list(input())
total = 0

for bit in range(1 << (N-1)):
  f = A[0]
  for i in range(N-1):
    if bit & (1 << i):
      f += '+'
    else:
      f += '-'
    f += A[i+1]
  total = eval(f)
  if total == 7:
    print(f+'=7')
    break
