import sys
input = sys.stdin.readline

MAX = 20
N = int(input()) - 1
[*info, answer] = list(map(int, input().split()))
dp = [[0 for _ in range(MAX + 1)] for n in range(N)]
dp[0][info[0]] = 1

for i in range(1, N):
    for j in range(MAX + 1):
        if 0 <= j + info[i] <= MAX:
            dp[i][j + info[i]] += (dp[i - 1][j])
        if 0 <= j - info[i] <= MAX:
            dp[i][j - info[i]] += (dp[i - 1][j])

print(dp[-1][answer])