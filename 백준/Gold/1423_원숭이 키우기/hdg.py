import sys
input = sys.stdin.readline

N = int(input())
characters = list(map(int, input().split()))
powers = list(map(int, input().split()))
D = int(input())

#N = 5
#characters = [1, 2, 3, 4, 5]
#powers = [1, 4, 9, 16, 25]
#D = 10

dp = [[[-1 for k in range(D + 1)] for level in range(N)] for day in range(D + 1)]

def dfs(day, level, curr):
    if level == N - 1:
        return 0;

    if dp[day][level][curr] > -1:
        return dp[day][level][curr]

    dp[day][level][curr] = 0
    for next in range(characters[level] + curr + 1):
        if day + next > D:
            break;
        dp[day][level][curr] = max(dp[day][level][curr], dfs(day + next, level + 1, next) + (powers[level + 1] - powers[level]) * next)
    return dp[day][level][curr]

print(sum(map(lambda level: characters[level] * powers[level], range(N))) + dfs(0, 0, 0))