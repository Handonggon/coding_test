import sys
input = sys.stdin.readline

N = int(input())
box = list(map(int, input().split()))

# N = 8
# box = [1, 6, 2, 5, 7, 3, 5, 6]

dp = [1] * N
for i in range(N):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))