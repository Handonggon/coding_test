import sys
input = sys.stdin.readline

INF = 1000000 * 20
[length, width, height] = list(map(int, input().split()))
n = int(input())
info = [0 for _ in range(21)]
for _ in range(n):
    [a, b] = list(map(int, input().split()))
    info[a] = b

def division(l, w, h):
    for t in range(n - 1, -1, -1):
        T = pow(2, t)
        if T > min(l, w, h):
            continue
        if info[t] == 0:
            continue
        info[t] -= 1
        return (0 if l - T == 0 else division(l - T, T, h))\
             + (0 if w - T == 0 else division(l, w - T, h))\
             + (0 if h - T == 0 else division(T, T, h - T))\
             + 1
    return -INF

answer = division(length, width, height)
print(answer) if answer > -1 else print(-1)