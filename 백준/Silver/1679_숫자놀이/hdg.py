import sys
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
K = int(input())

dp = [0]

curr = 0
while dp[-1] <= K:
    curr += 1

    if curr in info:
        dp.append(1)
        continue

    dp.append(K+1)
    for prev in info:
        if curr - prev >= 0:
            dp[curr] = min(dp[curr], dp[curr - prev] + 1)

print("jjaksoon win at {0}".format(curr)) if curr % 2 else print("holsoon win at {0}".format(curr))