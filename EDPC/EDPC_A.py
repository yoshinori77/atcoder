def solve():
    N = int(input())
    h = list(map(int, input().split()))
    dp = [float("inf")] * N
    dp[0] = 0
    dp[1] = abs(h[0] - h[1])
    h_2 = h[0]
    h_1 = h[1]

    for i in range(2, N):
        x = h[i]
        dp[i] = min(
            dp[i - 1] + abs(x - h_1),
            dp[i - 2] + abs(x - h_2)
        )
        h_2 = h_1
        h_1 = x
    return dp[-1]


if __name__ == "__main__":
    print(solve())