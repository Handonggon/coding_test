import sys
input = sys.stdin.readline

[W, H] = list(map(int, input().split()))
N = int(input())
isTile = [[False for h in range(H+1)] for w in range(W+1)]
for n in range(N):
    [x, y] = list(map(int, input().split()))
    isTile[x][y] = True

dp = [[0 for h in range(H+1)] for w in range(W+1)]

for w in range(W+1):
    for h in range(H+1):
        if isTile[w][h]:
            continue
        
        dp[w][h] = w * h
        for x in range(w//2 + 1):
            dp[w][h] = min(dp[w][h], dp[x][h] + dp[w - x][h])

        for y in range(h//2 + 1):
            dp[w][h] = min(dp[w][h], dp[w][y] + dp[w][h - y])

print(dp[W][H])