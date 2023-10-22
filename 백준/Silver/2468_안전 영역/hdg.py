import sys
input = sys.stdin.readline
from collections import deque

MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

def isMove(y, x):
    return 0 <= y < N and 0 <= x < N

answer = 0
for h in range(max(sum(info, []))):
    visited = [[info[y][x] <= h for x in range(N)] for y in range(N)]

    def bfs(y, x):
        queue = deque([[y, x]])
        visited[y][x] = True

        while queue:
            [y, x] = queue.popleft()
            for [dy, dx] in MOVE:
                if isMove(y + dy, x + dx):
                    if not visited[y + dy][x + dx]:
                        visited[y + dy][x + dx] = True
                        queue.append([y + dy, x + dx])
    count = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                count += 1
                bfs(y, x)
    answer = max(answer, count)

print(answer)