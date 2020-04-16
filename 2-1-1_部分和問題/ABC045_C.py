S = input()
N = len(S)
total = 0

for bit in range(1 << (N-1)):
  f = S[0]
  for i in range(N-1):
    if bit & (1 << i):
      f += '+'
    f += S[i+1]
  total += sum(map(int, f.split('+')))

print(total)
