import sys
input = sys.stdin.readline

DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]] #동 서 남 북

[N, *probability] = list(map(int, input().split()))
visited = [[False for j in range(2*N + 1)] for i in range(2*N + 1)]
visited[N][N] = True

def dfs(y, x, move, percent):
    answer = 0
    if move==0:
        return percent
    else:
        for direction in range(len(DIRECTION)):
            [ty, tx] = DIRECTION[direction]
            if not visited[y+ty][x+tx]:
                visited[y+ty][x+tx] = True
                answer += dfs(y+ty, x+tx, move-1, percent*probability[direction]*0.01)
                visited[y+ty][x+tx] = False
    return answer

print(dfs(N, N, N, 1))