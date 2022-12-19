import sys
input = sys.stdin.readline

N = int(input())
# N = 7

dp = [count for count in range(N+1)]

for number in range(N + 1):
    for target in range(1, int(number ** (1 / 2)) + 1):
        dp[number] = min(dp[number], 1 + dp[number - (target ** 2)])

print(dp[N])