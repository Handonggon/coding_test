import sys
input = sys.stdin.readline

dp = ["{}", "{{}}"]
for _ in range(20):
    dp.append(dp[-1][0:-1] + ',' + dp[-1] + '}')

T = int(input())
for t in range(T):
    print(dp[dp.index(input().strip()) + dp.index(input().strip())])