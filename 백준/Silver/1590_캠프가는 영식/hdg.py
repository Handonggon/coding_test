import sys
input = sys.stdin.readline

[N, T] = list(map(int, input().split()))
info = [list(map(int, input().split())) for n in range(N)]

# [N, T] = [1, 285]
# info = [[150, 50, 10]]

answer = []
for n in range(N):
    [S, I, C] = info[n]
    for c in range(C):
        if S + (I * c) >= T:
            answer.append(S + (I * c) - T)
print(min(answer) if answer else -1)