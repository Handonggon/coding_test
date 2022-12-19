import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for n in range(N)]

dp = [[0] * 3 for n in range(N + 1)]
for n in range(1, N + 1):
    for c in range(3):
        dp[n][c] = min(dp[n - 1][(c + 1) % 3] + info[n - 1][c], dp[n - 1][(c + 2) % 3] + info[n - 1][c])

print(min(dp[N]))