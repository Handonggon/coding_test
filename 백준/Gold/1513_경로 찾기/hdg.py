import sys
input = sys.stdin.readline

[N, M, C] = list(map(int, input().split()))
info = {n: {m: 0 for m in range(M+1)} for n in range(N+1)}
for c in range(C):
    [n, m] = list(map(int, input().split()))
    info[n][m] = c + 1

# [N, M, C] = [3, 3, 2]
# info = {n: {m: 0 for m in range(M+1)} for n in range(N+1)}
# for [n, m, c] in [[2, 2, 1], [3, 2, 2]]:
#     info[n][m] = c

dp = [[[[-1 for count in range(C+1)] for curr in range(C+1)] for m in range(M+1)] for n in range(N+1)]
if info[1][1] == 0:
    dp[1][1][0][0] = 1
else:
    dp[1][1][info[1][1]][1] = 1

def dfs(n, m, curr, count):
    if (n < 1 or n > N or m < 1 or m > M):
        return 0

    if dp[n][m][curr][count] > -1:
        return dp[n][m][curr][count]

    dp[n][m][curr][count] = 0
    if info[n][m] == 0:
        dp[n][m][curr][count] = dfs(n-1, m, curr, count) + dfs(n, m-1, curr, count) % 1000007
    elif info[n][m] == curr:
        for prev in range(curr):
            dp[n][m][curr][count] += (dfs(n-1, m, prev, count - 1) + dfs(n, m-1, prev, count - 1)) % 1000007
    return dp[n][m][curr][count]

for count in range(C+1):
    answer = 0
    for curr in range(C+1):
        answer = (answer + dfs(N, M, curr, count)) % 1000007
    print(answer, end=" ")