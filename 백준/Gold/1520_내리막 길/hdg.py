import sys
input = sys.stdin.readline

MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]

[N, M] = list(map(int, input().split()))
info = [list(map(int, input().split())) for n in range(N)]

dp = [[-1 for m in range(M)] for n in range(N)]

def dfs(y, x):
    if y == N - 1 and x == M - 1:
        return 1

    if dp[y][x] > -1:
        return dp[y][x]

    dp[y][x] = 0
    for [dy, dx] in MOVE:
        if y + dy >= 0 and y + dy < N and x + dx >= 0 and x + dx < M:
            if info[y][x] > info[y + dy][x + dx]:
                dp[y][x] += dfs(y + dy, x + dx)
    return dp[y][x]
print(dfs(0, 0))