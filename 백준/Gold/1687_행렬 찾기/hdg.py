import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))

dp = [[0] for n in range(N)]
for n in range(N):
    for item in list(input().strip()):
        dp[n].append(dp[n][-1] + 1 if item == '0' else 0)

answer = 0
for n in range(N):
    for m in range(1, M + 1):
        if dp[n][m] == 0:
            continue  
        width = 333
        for k in range(n, -1, -1):
            width = min(width, dp[k][m])
            if width == 0:
                break
            answer = max(answer, (n - k + 1) * width)
print(answer)