import sys
input = sys.stdin.readline
from collections import deque

[Y, X] = [0, 1]
MOVE = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
T = int(input())
for _ in range(T):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    def isMove(y, x):
        return 0 <= y < l and 0 <= x < l
    visited = [[False for _ in range(l)] for _ in range(l)]
    queue = deque([[start[Y], start[X], 0]])
    visited[start[Y]][start[X]] = True

    while queue:
        [y, x, cost] = queue.popleft()
        if y == end[Y] and x == end[X]:
            print(cost)
            break

        for [dy, dx] in MOVE:
            if isMove(y + dy, x + dx) and not visited[y + dy][x + dx]:
                visited[y + dy][x + dx] = True
                queue.append([y + dy, x + dx, cost + 1])