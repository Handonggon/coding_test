import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    info = [list(sorted(map(int, input().split()))) for n in range(N)]
    
    dp = [0 for _ in range(201)]
    for [start, end] in info:
        for index in range((start + 1) // 2, ((end + 1) // 2) + 1):
            dp[index] += 10
    print(max(dp))