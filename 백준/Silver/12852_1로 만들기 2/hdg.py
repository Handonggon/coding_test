import sys
input = sys.stdin.readline

N = int(input())

dp = [[] for _ in range(N + 1)]
dp[1] = [1]
for index in range(2, N + 1):
    answer = []
    if index % 3 == 0:
        answer.append([index] + dp[index // 3])
    if index % 2 == 0:
        answer.append([index] + dp[index // 2])
    answer.append([index] + dp[index - 1])

    dp[index] = sorted(answer, key = lambda item: len(item))[0]
print(len(dp[N]) - 1)
print(*dp[N])