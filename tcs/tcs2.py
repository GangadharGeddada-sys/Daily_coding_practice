def count_sequences(N, R, end):
    dp = [[0] * (R + 1) for _ in range(N + 1)]

    dp[1][1] = 1
    total = [0] * (N + 1)
    total[1] = 1

    for i in range(2, N + 1):
        for j in range(1, R + 1):
            dp[i][j] = total[i-1] - dp[i-1][j]
        total[i] = sum(dp[i])

    return dp[N][end]


# Example
print(count_sequences(4, 4, 3))  # Output: 7