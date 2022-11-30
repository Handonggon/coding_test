import sys
input = sys.stdin.readline

N = int(input())

dp = [0, 1]
for n in range(2, N+1):
    dp.append(dp[-1] + (n // 6) - (n % 6 == 1) + 1)
print(dp[N])