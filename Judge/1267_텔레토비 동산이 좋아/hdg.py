MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]

K = int(input())
[M, N] = list(map(int, input().split()))
[r, c] = list(map(int, input().split()))

def isBound(y, x):
    return y >= 0 and x >= 0 and y < M and x < N


dp = [[[-1 for x in range(N)] for y in range(M)] for k in range(K)]

def dfs(y, x, c):
    if c == K:
        return 0
    
    if dp[c][y][x] == -1:
        summary = 0
        for [dy, dx] in MOVE:
            if isBound(y + dy, x + dx):
                summary += dfs(y + dy, x + dx, c + 1)
            else:
                summary += 1
        dp[c][y][x] = summary % 1000000007

    return dp[c][y][x]

print(dfs(r, c, 0))