m = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0
for c in coins:
    n = m // c
    m -= c * n
    count += n
print(count)