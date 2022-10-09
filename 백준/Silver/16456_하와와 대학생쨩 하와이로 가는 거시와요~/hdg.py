n = int(input())

dp = [0 for _ in range(max(n, 3))]
dp[0] = dp[1] = 1
dp[2] = 2

for i in range(3, n):
    dp[i] = (dp[i-3] + dp[i-1]) % 1000000009

print(dp[n-1])