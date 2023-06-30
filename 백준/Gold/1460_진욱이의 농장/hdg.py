import sys
input = sys.stdin.readline

[N, M] = map(int, input().split())
farm = [[0 for c in range(N)] for r in range(N)]
for _ in range(M):
    [X, Y, L, F] = map(int, input().split())
    for r in range(L):
        for c in range(L):
            farm[Y + r][X + c] = F

answer = 0
for one in range(1, 8):
    for two in range(one, 8):
        dp = [[int(farm[r][c] == one or farm[r][c] == two) for c in range(N)] for r in range(N)]
        for r in range(1, N):
            for c in range(1, N):
                if dp[r][c] > 0:
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
                    answer = max(answer, dp[r][c])
print(answer * answer)