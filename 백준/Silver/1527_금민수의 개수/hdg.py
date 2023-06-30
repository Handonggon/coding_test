import sys
input = sys.stdin.readline

[A, B] = map(int, input().split())
answer = 0
dp = [[] for _ in range(len(str(B)) + 1)]
dp[0] = [0]
for i in range(1, len(dp)):
    for num in dp[i-1]:
        dp[i].append(num * 10 + 4)
        dp[i].append(num * 10 + 7)

    for num in dp[i]:
        if A <= num <= B:
            answer += 1
print(answer)