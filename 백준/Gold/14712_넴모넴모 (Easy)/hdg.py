import sys
input = sys.stdin.readline

[N, M] = map(int, input().split())
board = [[False for _ in range(M)] for _ in range(N)]

def dfs(curr):
    [y, x] = [curr // M, curr % M]
    if curr >= N * M:
        return 1

    answer = 0
    board[y][x] = False
    answer += dfs(curr + 1)
    if y > 0 and x > 0:
        if board[y - 1][x - 1] and board[y][x - 1] and board[y - 1][x]:
            return answer
    board[y][x] = True
    answer += dfs(curr + 1)
    return answer

print(dfs(0))