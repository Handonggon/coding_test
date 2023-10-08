import sys
from collections import deque
input = sys.stdin.readline

MOVE = [[0, 0, -1], [0, -1, 0], [0, 0, 1], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]

while True:
    [L, R, C] = map(int, input().split())
    if L == R == C == 0:
        break
    def isMove(l, r, c):
        return 0 <= l < L and 0 <= r < R and 0 <= c < C

    board = []
    for l in range(L):
        board.append([list(input().strip()) for r in range(R)])
        input()

    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    queue = deque()
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if board[l][r][c] == 'S':
                    visited[l][r][c] = True
                    queue.append([l, r, c, 0])
    
    answer = -1
    while queue:
        [l, r, c, cost] = queue.popleft()
        if board[l][r][c] == 'E':
            answer = cost
            break

        for [dl, dr, dc] in MOVE:
            if isMove(l + dl, r + dr, c + dc):
                if board[l + dl][r + dr][c + dc] == '#':
                    continue
                if visited[l + dl][r + dr][c + dc]:
                    continue
                visited[l + dl][r + dr][c + dc] = True
                queue.append([l + dl, r + dr, c + dc, cost + 1])
    
    print("Escaped in {0} minute(s).".format(answer)) if answer > -1 else print("Trapped!")