import sys
input = sys.stdin.readline

D = int(input())
adj = [[0, 1, 1, 0, 0, 0, 0, 0]
     , [1, 0, 1, 1, 0, 0, 0, 0]
     , [1, 1, 0, 1, 1, 0, 0, 0]
     , [0, 1, 1, 0, 1, 1, 0, 0]
     , [0, 0, 1, 1, 0, 1, 1, 0]
     , [0, 0, 0, 1, 1, 0, 0, 1]
     , [0, 0, 0, 0, 1, 0, 0, 1]
     , [0, 0, 0, 0, 0, 1, 1, 0]]

dp = [[0 for c in range(D + 1)] for r in range(8)]
dp[0][0] = 1
for d in range(1, D + 1):
    for next in range(8):
        for prev in range(8):
            if adj[prev][next]:
                dp[next][d] += dp[prev][d - 1]
                dp[next][d] = dp[next][d] % 1000000007

print(dp[0][D])