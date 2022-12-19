import sys
input = sys.stdin.readline

dp = [0, 1, 2]
for n in range(40):
    dp.append(dp[-2] + dp[-1])

N = int(input())
M = int(input())
info = [0] + [int(input()) for m in range(M)] + [N + 1]

# N = 9
# M = 2
# info = [0] + [4, 7] + [N + 1]

answer = 1
for index in range(1, M + 2):
    count = info[index] - info[index - 1] - 1
    if count == 0:
        continue
    answer = answer * dp[count]
print(answer)