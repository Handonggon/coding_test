import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 3, 7]

for n in range(3, N + 1):
    dp.append((dp[n - 2] + 2 * dp[n - 1]) % 9901)
print(dp[N])