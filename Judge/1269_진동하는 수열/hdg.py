import sys
input = sys.stdin.readline

#N = int(input())
#info = list(map(int, input().split()))

N = 5
info = [1, 2, 3, 2, 1]

# i번째 인덱스로 증가/감소하면서 끝나는 진동하는 수열의 최대 길이
dp = [[0, 0] for _ in range(N+1)]

for i in range(N):
    for j in range(i):
        if info[i] == info[j]:
            continue
    
        if info[j] < info[i]:
            dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        else:
            dp[i][1] = max(dp[i][1], dp[j][0] + 1)

print(N - (max(dp[N-1]) + 1))

#[0..i] 구간에서 증가/감소로 끝나는 진동하는 수열의 최대 길이

dp = [1, 1]

for i in range(1, N):
    if info[i-1] == info[i]:
        continue

    if info[i-1] < info[i]:
        dp[0] = dp[1] + 1
    else:
        dp[1] = dp[0] + 1
    
print(N - max(dp))