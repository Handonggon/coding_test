import sys
input = sys.stdin.readline

INF = 1000000001

fibo = [1, 2]
while fibo[-1] < INF:
    fibo.append(fibo[-2] + fibo[-1])
print(len(fibo))
T = int(input())
for _ in range(T):
    n = int(input())
    answer = []

    while n > 0:
        for i in range(len(fibo) - 1, -1, -1):
            if fibo[i] <= n:
                n -= fibo[i]
                answer.append(fibo[i])
                break
    print(*reversed(answer))