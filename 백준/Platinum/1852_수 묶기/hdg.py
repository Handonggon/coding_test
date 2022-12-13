import sys
input = sys.stdin.readline
INF = 3000000000

# N = int(input())
# board = [list(map(int, input().split())) for n in range(N)]

N = 4
board = [[3, 8, 5], [4, 12, 10], [9, 7, 5], [6, 2, 8]] # 29 15
W = len(board[0])

if True:
    dp = [[-1 for state in range(1 << 3)] for n in range(N * W)]

    def dfs(pos, state):
        if pos == (N * W):
            return 0
        if dp[pos][state] > -1:
            return dp[pos][state]

        dp[pos][state] = -INF
        [y, x] = [pos // W, pos % W]
        if state & 1:
            dp[pos][state] = dfs(pos + 1, state >> 1)
        else :
            if y < N - 1:
                dp[pos][state] = max(dp[pos][state], dfs(pos + 1, (state >> 1) | (1 << 2)) + abs(board[y][x] - board[y + 1][x]))
            if (x < W - 1) and not (state & 2):
                dp[pos][state] = max(dp[pos][state], dfs(pos + 2, state >> 2) + abs(board[y][x] - board[y][x + 1]))
        return dp[pos][state]

    print(dfs(0, 0))

if True:
    dp = [[-1 for state in range(1 << 3)] for n in range(N * 3)]

    def dfs(pos, state):
        if pos == (N * W):
            return 0
        if dp[pos][state] > -1:
            return dp[pos][state]

        dp[pos][state] = INF
        [y, x] = [pos // W, pos % W]
        if state & 1:
            dp[pos][state] = dfs(pos + 1, state >> 1)
        else :
            if y < N - 1:
                dp[pos][state] = min(dp[pos][state], dfs(pos + 1, (state >> 1) | (1 << 2)) + abs(board[y][x] - board[y + 1][x]))
            if (x < W - 1) and not (state & 2):
                dp[pos][state] = min(dp[pos][state], dfs(pos + 2, state >> 2) + abs(board[y][x] - board[y][x + 1]))
        return dp[pos][state]

    print(dfs(0, 0))