import sys
input = sys.stdin.readline

[Y, X] = [0, 1]
MOVE = [[-1, 0], [0, 1], [1, 0], [0, -1]]

[W, H] = list(map(int, input().split()))
info = [list(input().strip()) for h in range(H)]

loc = []
for h in range(H):
    for w in range(W):
        if info[h][w] == 'C':
            loc.append([h, w])
            info[h][w] = '.'
start = loc[0]
end = loc[1]

dp = [[[(W * H) for _ in range(len(MOVE))] for w in range(W)] for h in range(H)]

stack = [[start[Y], start[X], d, 0] for d in range(len(MOVE))]
while stack:
    [y, x, d, c] = stack.pop()

    for move in range(-1, 2):
        dd = (len(MOVE) + d + move) % len(MOVE)
        [dy, dx] = MOVE[dd]
        if 0 <= y + dy < H and 0 <= x + dx < W and info[y + dy][x + dx] == '.':
            if dp[y + dy][x + dx][dd] > c + abs(move):
                stack.append([y + dy, x + dx, dd, c + abs(move)])
                dp[y + dy][x + dx][dd] = c + abs(move)

print(min(dp[end[0]][end[1]]))