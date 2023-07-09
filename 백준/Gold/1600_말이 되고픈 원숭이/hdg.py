import sys
from collections import deque
input = sys.stdin.readline

MONKEY = [(0, -1), (-1, 0), (0, 1), (1, 0)]
HORSE = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

K = int(input())
[W, H] = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

# K = 1
# [W, H] = [4, 4]
# board = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]

def isMove(y, x):
    return (0 <= y < H and 0 <= x < W and board[y][x] == 0)

def bfs():
    visited = [[[False for k in range(K + 1)] for w in range(W)] for h in range(H)]
    queue = deque([[0, 0, 0, 0]])
    while queue:
        [y, x, c, k] = queue.popleft()
        if y == H - 1 and x == W - 1:
            return c
        if visited[y][x][k]:
            continue
        visited[y][x][k] = True
        
        if k < K:
            for (dy, dx) in HORSE:
                if isMove(y + dy, x + dx):
                    queue.append([y + dy, x + dx, c + 1, k + 1])
        for (dy, dx) in MONKEY:
                if isMove(y + dy, x + dx):
                    queue.append([y + dy, x + dx, c + 1, k])
    return -1
print(bfs())