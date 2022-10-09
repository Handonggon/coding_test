import sys
from collections import deque

MOVE = [[1, 0], [0, 1]]

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

isBound = lambda y, x: y > -1 and y < N and x > -1 and x < N

queue = deque()
queue.append((0, 0))
visited = [[False for _ in range(N)] for _ in range(N)]

while len(queue):
    (y, x) = queue.popleft()
    visited[y][x] = True
    if board[y][x] == -1:
        break

    for move in MOVE:
        [dy, dx] = list(map(lambda d: d * board[y][x], move))
        if isBound(y+dy, x+dx) and not visited[y+dy][x+dx]:
            queue.append((y+dy, x+dx))

print('HaruHaru') if visited[N-1][N-1] else print('Hing')
