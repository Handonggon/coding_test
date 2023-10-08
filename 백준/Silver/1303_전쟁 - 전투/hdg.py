import sys
from collections import deque
input = sys.stdin.readline

MOVE = [[0, 1], [-1, 0], [0, -1], [1, 0]]
[N, M] = map(int, input().split())
board = [list(map(str, input().strip())) for m in range(M)]

answer = {'W': 0, 'B': 0}
visited = [[False for n in range(N)] for m in range(M)]

def isMove(m, n):
    return 0 <= m < M and 0 <= n < N

for m in range(M):
    for n in range(N):
        if visited[m][n]:
            continue

        count = 1
        target = board[m][n]
        queue = deque([[m, n]])
        visited[m][n] = True
        while queue:
            [m, n] = queue.popleft()

            for [dm, dn] in MOVE:
                if isMove(m + dm, n + dn):
                    if visited[m + dm][n + dn]:
                        continue
                    if board[m + dm][n + dn] == target:
                        count += 1
                        queue.append([m + dm, n + dn])
                        visited[m + dm][n + dn] = True
        answer[target] += (count * count)
print("{0} {1}".format(answer['W'], answer['B']))