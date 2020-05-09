import numpy as np


def solve():
    N, K = map(int, input().split())
    h = np.array(list(map(int, input().split())))
    dp = np.full(N, 10**9, dtype=np.int)
    dp[0] = 0

    for i in range(1, N):
        dp[i:i + K] = np.fmin(
            dp[i:i + K],
            dp[i - 1] + np.abs(h[i:i + K] - h[i - 1])
        )
    return dp[-1]


if __name__ == "__main__":
    print(solve())
