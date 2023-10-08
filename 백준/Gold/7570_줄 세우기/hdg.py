import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N + 1)]
for num in list(map(int, input().split())):
    dp[num] = dp[num - 1] + 1
print(N - max(dp))