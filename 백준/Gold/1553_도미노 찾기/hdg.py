import sys
input = sys.stdin.readline

domino = [[False for j in range(6 + 1)] for i in range(6 + 1)]
answer = [list(map(int, list(input().strip()))) for _ in range(8)]
visited = [[False for c in range(7)] for r in range(8)]

def dfs(curr):
    if curr == 56:
        return 1
    y = curr // 7
    x = curr % 7
    if visited[y][x]:
        return dfs(curr + 1)
    
    count = 0
    visited[y][x] = True
    for (dy, dx) in [(0, 1), (1, 0)]:
        if y + dy < 8 and x + dx < 7:
            if visited[y + dy][x + dx]:
                continue
            if domino[answer[y][x]][answer[y + dy][x + dx]]:
                continue
            domino[answer[y][x]][answer[y + dy][x + dx]] = domino[answer[y + dy][x + dx]][answer[y][x]] = True
            visited[y + dy][x + dx] = True
            count += dfs(curr + 1)
            visited[y + dy][x + dx] = False
            domino[answer[y][x]][answer[y + dy][x + dx]] = domino[answer[y + dy][x + dx]][answer[y][x]] = False
    visited[y][x] = False
    return count
    
print(dfs(0))