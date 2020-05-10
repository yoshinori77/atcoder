def solve():
    N = int(input())
    p = list(map(int, input().split()))
    bit = 1
    for i in range(N):
        bit |= (bit << p[i])
    return bin(bit).count("1")


if __name__ == "__main__":
    print(solve())
