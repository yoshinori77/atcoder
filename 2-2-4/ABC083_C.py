X, Y = map(int, input().split())
z = 0
count = 1
while True:
    z = X * 2
    if z <= Y:
        count += 1
    else:
        break
print(count)