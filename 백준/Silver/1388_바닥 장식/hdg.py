import sys
input = sys.stdin.readline

[N, M] = map(int, input().split())
board = [input().rstrip() for i in range(N)]

answer = 0
for n in range(N):
    for m in range(M):
        if board[n][m] == '-':
            if m > 0 and board[n][m - 1] == '-':
                continue
        if board[n][m] == '|':
            if n > 0 and board[n - 1][m] == '|':
                continue
        answer += 1
print(answer)