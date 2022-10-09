#Brute Force    ->  시간초과
MAX = 1000 * 100

[C, N] = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(N)]

stack = [(0, 0)]

amswer = MAX
while stack:
    [money, count] = stack.pop()
    if count >= C:
        amswer = min(amswer, money)
        continue

    for [cost, profit] in info:
        stack.append((money+cost, count+profit))

print(amswer)


#Back Tracking  ->  30840KB, 384ms
MAX = 1000 * 100

[C, N] = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(N)]

dp = [MAX for _ in range(C+1)]
stack = [(0, 0)]

while stack:
    [money, count] = stack.pop()

    for [cost, profit] in info:
        if dp[min(C, count + profit)] > money + cost:
            dp[min(C, count + profit)] = money + cost
            stack.append((money + cost, count + profit))

print(dp[C])

#Dynamic Programming    ->  33668KB, 144ms
MAX = 1000 * 100

[C, N] = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(MAX+1)]
for [cost, profit] in info:
    dp[cost] = profit


for money in range(len(dp)):
    for [cost, profit] in info:
        if money-cost >= 0:
            dp[money] = max(dp[money], dp[money-cost] + profit)

    if(dp[money] >= C):
        print(money)
        break;