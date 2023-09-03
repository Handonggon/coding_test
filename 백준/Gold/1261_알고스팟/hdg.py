import sys
import heapq
input = sys.stdin.readline

INF = 100 * 100 + 1
MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]
[M, N] = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

def isMove(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs(y, x):
    heap = [(0, y, x)]
    dp = [[INF for m in range(M)] for n in range(N)]
    dp[y][x] = 0

    while heap:
        (c, y, x) = heapq.heappop(heap)
        
        for [dy, dx] in MOVE:
            if isMove(y + dy, x + dx) and dp[y + dy][x + dx] > board[y + dy][x + dx] + dp[y][x]:
                dp[y + dy][x + dx] = board[y + dy][x + dx] + dp[y][x]
                heapq.heappush(heap, (dp[y + dy][x + dx], y + dy, x + dx))
    return dp[N - 1][M - 1]
print(bfs(0, 0))