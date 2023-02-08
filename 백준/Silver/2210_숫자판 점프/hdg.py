import sys
input = sys.stdin.readline

MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]
[H, W, L] = [5, 5, 6]

info = [input().split() for _ in range(H)]

dp = [[[set([info[h][w]]) if l == L - 1 else set() for w in range(W)] for h in range(H)] for l in range(L)]

def dfs(y, x, length):    
    if dp[length][y][x]:
        return dp[length][y][x]

    for [dy, dx] in MOVE:
        if 0 <= y + dy < W and 0 <= x + dx < H:
            dp[length][y][x].update(map(lambda item: int(str(item) + info[y][x]), dfs(y + dy, x + dx, length + 1)))
    return dp[length][y][x]

answer = set()
for h in range(H):
    for w in range(W):
        answer.update(dfs(h, w, 0))
print(len(answer))