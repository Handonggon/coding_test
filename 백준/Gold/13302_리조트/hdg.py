import sys
input = sys.stdin.readline

INF = 1000000
[N, M] = map(int, input().split())
holiday = []
if M > 0:
    holiday = list(map(int, input().split()))

dp = [[INF for _ in range(40 + 10)] for _ in range(N + 10)]
dp[0][0] = 0

for day in range(N + 1):
    for coupon in range(40):
        curr = dp[day][coupon]
        if curr == INF:
            continue
        
        if (day + 1) in holiday:
            dp[day + 1][coupon] = min(curr, dp[day + 1][coupon])
        # 쿠폰
        if coupon >= 3:
            dp[day + 1][coupon - 3] = min(curr, dp[day + 1][coupon - 3])
        # 1일권
        dp[day + 1][coupon] = min(curr + 10000, dp[day + 1][coupon])
        # 3일권
        for next in range(1, 4):
            dp[day + next][coupon + 1] = min(curr + 25000, dp[day + next][coupon + 1])
        # 5일권
        for next in range(1, 6):
            dp[day + next][coupon + 2] = min(curr + 37000, dp[day + next][coupon + 2])
print(min(dp[N]))