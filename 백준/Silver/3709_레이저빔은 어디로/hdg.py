import sys
input = sys.stdin.readline

MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]

T = int(input())
for _ in range(T):
    [N, R] = list(map(int, input().split()))
    box = [[False for x in range(N + 2)] for y in range(N + 2)]
    for r in range(R):
        [y, x] = list(map(int, input().split()))
        box[y][x] = True
    [y, x] = list(map(int, input().split()))

    if y == 0:
        m = 3
    if y == N + 1:
        m = 1
    if x == 0:
        m = 2
    if x == N + 1:
        m = 0

    visited = [[[False for m in range(4)] for x in range(N + 2)] for y in range(N + 2)]

    while not visited[y][x][m]:
        visited[y][x][m] = True

        if box[y][x]:
            m = (m + 1) % 4

        y = y + MOVE[m][0]
        x = x + MOVE[m][1]
        if y == 0 or y == (N + 1) or x == 0 or x == (N + 1):
            break

    if visited[y][x][m]:
        print(0, 0)
    else:
        print(y, x)