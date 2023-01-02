import sys
input = sys.stdin.readline

N = int(input())

dp = [[[-1 for a in range(3)] for l in range(2)] for o in range(N + 1)]

def dfs(o, l, a):
    if l == 2 or a == 3:
        return 0

    if o == N:
        dp[o][l][a] = 1
        return dp[o][l][a]

    if dp[o][l][a] > -1:
        return dp[o][l][a]

    dp[o][l][a] = 0
    dp[o][l][a] += (dfs(o + 1, l, 0) % 1000000)
    dp[o][l][a] += (dfs(o + 1, l + 1, 0) % 1000000)
    dp[o][l][a] += (dfs(o + 1, l, a + 1) % 1000000)
    return dp[o][l][a]

print(dfs(0, 0, 0) % 1000000)