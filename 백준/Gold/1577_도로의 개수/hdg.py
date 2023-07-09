import sys
input = sys.stdin.readline

[N, M] = map(int, input().split())
K = int(input())
construction = [[False for c in range(2 * N + 1)] for r in range(2 * M + 1)]
for _ in range(K):
    [a, b, c, d] = map(int, input().split())
    construction[b + d][a + c] = True

dp = [[0 for c in range(N + 1)] for r in range(M + 1)]
for r in range(M + 1):
    if construction[2 * r - 1][0]: break
    dp[r][0] = 1
for c in range(N + 1):
    if construction[0][2 * c - 1]: break
    dp[0][c] = 1

for r in range(1, M + 1):
    for c in range(1, N + 1):
        if not construction[2 * r - 1][2 * c]:
            dp[r][c] += dp[r - 1][c]
        if not construction[2 * r][2 * c - 1]:
            dp[r][c] += dp[r][c - 1]
print(dp[M][N])