[N, S, M] = list(map(int, input().split()))
difference = [0] + list(map(int, input().split()))

dp = [[False for c in range(M+1)] for r in range(N+1)]
dp[0][S] = True

for index in range(1, N+1):
    for volume in range(M+1):
        if dp[index-1][volume]:
            if volume + difference[index] <= M:
                dp[index][volume + difference[index]] = True
            if volume - difference[index] >= 0:
                dp[index][volume - difference[index]] = True

answer = -1
for volume in range(M+1):
    if dp[N][volume]:
        answer = volume
print(answer)