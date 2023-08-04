import sys
from collections import deque
input = sys.stdin.readline

[R, C] = map(int, input().split())
INF = R * C + 1
board = [list(map(int, input().split())) for r in range(R)]
N = int(input())
MOVE = [list(map(int, input().split())) for _ in range(N)]

def isMove(r, c):
    return 0 <= r < R and 0 <= c < C and board[r][c] == 1

def bfs():
    visited = [[False for c in range(C)] for r in range(R)]
    queue = deque([])
    for c in range(C):
        if board[0][c] == 1:
            queue.append([0, c, 0])
            visited[0][c] = True
    
    while queue:
        [r, c, cost] = queue.popleft()
        if r == R - 1:
            return cost
        for [dr, dc] in MOVE:
            if isMove(dr + r, dc + c) and not visited[dr + r][dc + c]:
                queue.append([dr + r, dc + c, cost + 1])
                visited[dr + r][dc + c] = True
    return -1

print(bfs())