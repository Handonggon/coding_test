[M, N] = list(map(int, input().split()))
F = int(input())
fInfo = [list(map(int, input().split())) for _ in range(F)]
B = int(input())
bInfo = [list(map(int, input().split())) for _ in range(B)]

map = [[0 for y in range(N)] for x in range(M)]

MOVE = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def isBound(x, y):
    return x >= 0 and y >= 0 and x < M and y < N

for [x, y] in bInfo:
    map[x][y] = pow(2, len(MOVE)) - 1

for [x, y] in fInfo:
    map[x][y] = pow(2, len(MOVE)) - 1
    for i in range(len(MOVE)):
        [dx, dy] = [x, y]
        while True:
            [dx, dy] = [MOVE[i][0] + dx, MOVE[i][1] + dy]
            if isBound(dx, dy) and (map[dx][dy] & (1 << i)) == 0:
                map[dx][dy] |= (1 << i)
            else:
                break

answer = 0
for x in range(M):
    for y in range(N):
        if map[x][y] == 0:
            answer += 1
print(answer)