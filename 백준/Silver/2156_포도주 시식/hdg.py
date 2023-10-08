import sys
input = sys.stdin.readline

n = int(input())
info = [0, 0, 0] + [int(input()) for _ in range(n)]
dp = [0, 0, 0]

for i in range(3, len(info)):
    dp.append(max(dp[i - 1], dp[i - 2] + info[i], dp[i - 3] + info[i - 1] + info[i]))

print(dp[-1])