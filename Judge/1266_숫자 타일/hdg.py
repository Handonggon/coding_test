MOVE = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

N = int(input())
info = [list(input()) for _ in range(N)]

dp = [0 for _ in range(N)]
for y in range(N):
    for x in range(N):
        for [dy, dx] in MOVE:
            number = ''
            for c in range(N):
                number += str(info[(N + y + (dy * c)) % N][(N + x + (dx * c)) % N])
                if int(number) < dp[c]:
                    break
                dp[c] = int(number)

print(dp[N-1])