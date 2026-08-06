N = int(input())
X = int(input())
I = int(input())

def solution():
    dp = [0] * (N + 1)
    dp[I] = 1

    window_sum = 1

    for i in range(I + 1, N + 1):
        dp[i] = window_sum

        if i - (X + 1) >= I:
            window_sum -= dp[i - (X + 1)]

        window_sum += dp[i]

    return dp[N]

print(solution())
