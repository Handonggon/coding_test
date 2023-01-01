import sys
input = sys.stdin.readline

[N, D] = list(map(int, input().split()))
info = {}
for n in range(N):
    [start, end, dist] = list(map(int, input().split()))
    if end not in info:
        info[end] = []
    info[end].append([start, dist])

dp = [d for d in range(D + 1)]

for d in range(D + 1):
    dp[d] = min(dp[d], dp[d - 1] + 1)
    if d in info:
        for [s, dist] in info[d]:
            dp[d] = min(dp[d], dp[s] + dist)

print(dp[-1])