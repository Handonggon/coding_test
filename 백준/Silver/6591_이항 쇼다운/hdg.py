import sys
input = sys.stdin.readline


while True:
    [n, k] = map(int, input().split())
    if n == k == 0:
        break

    div = 1
    answer = 1
    for _ in range(min(k, n - k)):
        answer *= n
        n -= 1
        answer /= div
        div += 1
    print(int(answer))