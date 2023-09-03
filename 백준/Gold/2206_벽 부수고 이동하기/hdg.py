import sys
from collections import deque
input = sys.stdin.readline

[ON, OFF] = [0, 1]
MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]
[N, M] = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

def isMove(y, x):
    return 0 < y <= N and 0 < x <= M

def bfs(y, x):
    visited = [[[False for m in range(M + 1)] for n in range(N + 1)] for _ in range(2)]
    queue = deque([[y, x, ON, 1]])
    visited[ON][y][x] = True

    while queue:
        [y, x, m, c] = queue.popleft()
        if y == N and x == M:
            return c
        for [dy, dx] in MOVE:
            if isMove(y + dy, x + dx):
                if board[y + dy - 1][ x + dx - 1] == '1' and m == ON and (not visited[OFF][y + dy][x + dx]):
                    visited[OFF][y + dy][x + dx] = True
                    queue.append([y + dy, x + dx, OFF, c + 1])
                if board[y + dy - 1][x + dx - 1] == '0' and not visited[m][y + dy][x + dx]:
                    visited[m][y + dy][x + dx] = True
                    queue.append([y + dy, x + dx, m, c + 1])
    return -1

print(bfs(1, 1))