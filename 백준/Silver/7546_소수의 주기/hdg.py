import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    print("Scenario #{0}:".format(t))
    [b, x, y] = list(input().split())
    b = int(b)
    x = int(x, b)
    y = int(y, b)

    dp = [0 for _ in range(y)]
    count = 1
    rem = x % y
    while dp[rem] == 0:
        dp[rem] = count
        rem = (rem * b) % y
        count += 1
    
    print(0 if rem == 0 else count - dp[rem])
    print()