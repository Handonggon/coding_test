import sys
input = sys.stdin.readline

T = 3
MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]

[R, C] = [5, 5]
INF = R * C

info = [list(map(int, input().split())) for _ in range(R)]
[r, c] = list(map(int, input().split()))

visited = [[False for c in range(C)] for r in range(R)]

def dfs(y, x, c, t):
    if t == T:
        return c
    
    reslut = INF
    visited[y][x] = True
    for [dy, dx] in MOVE:
        if 0 <= y + dy < R and 0 <= x + dx < C and not visited[y + dy][x + dx]:
            if info[y + dy][x + dx] == 0:
                reslut = min(reslut, dfs(y + dy, x + dx, c + 1, t))
            elif info[y + dy][x + dx] == 1:
                reslut = min(reslut, dfs(y + dy, x + dx, c + 1, t + 1))
    visited[y][x] = False
    return reslut

answer = dfs(r, c, 0, 0)
print(answer if answer < INF else -1)