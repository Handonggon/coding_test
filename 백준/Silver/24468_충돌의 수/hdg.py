import sys
input = sys.stdin.readline

[LOC, DIRE] = [0, 1]
MOVE = {'L': -1, 'R': 1}
[L, N, T] = map(int, input().split())
info = []
for _ in range(N):
    [loc, dire] = input().split()
    info.append([int(loc), MOVE[dire]])

answer = 0
for _ in range(T + 1):
    count = [0 for _ in range(L + 1)]
    for [loc, dire] in info:
        count[loc] += 1
        if count[loc] > 1:
            answer += 1
            
    for i in range(N):
        [loc, dire] = info[i]
        if loc == 0 or loc == L or count[loc] > 1:
            info[i] = [loc + (-1 * dire), -1 * dire]
        else:
            info[i] = [loc + dire, dire]
print(answer)