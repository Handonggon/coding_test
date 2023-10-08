import sys
input = sys.stdin.readline

[W, V] = [0, 1]
[N, K] = map(int, input().split())
info = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for n in range(1, N + 1):
    for k in range(1, K + 1):
        if k >= info[n][W]:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - info[n][W]] + info[n][V])
        else:
            dp[n][k] = dp[n - 1][k]

print(dp[N][K])