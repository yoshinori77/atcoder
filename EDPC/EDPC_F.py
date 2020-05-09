import numpy as np

t = np.array(list(input()), dtype='U1')
s = np.array(list(input()), dtype='U1')

ls = len(s)
lt = len(t)

eq = s[:, None] == t[None, :]
dp = [np.zeros(lt + 1, dtype=np.int16)]

# solve
for i in range(ls):
    prev = dp[-1].copy()
    np.maximum(prev[1:], prev[:-1] + eq[i], out=prev[1:])
    np.maximum.accumulate(prev, out=prev)
    dp.append(prev)

# print([list(line) for line in dp])

# restore
res = ''
i, j = ls, lt
while i > 0 and j > 0:
    if eq[i - 1][j - 1]:
        res += s[i - 1]
        i, j = i - 1, j - 1
        continue

    if dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(res[::-1])
