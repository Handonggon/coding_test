import sys
input = sys.stdin.readline

MOVE = [[0, -1], [-1, 0], [0, 1], [1, 0]]

T = int(input())
for _ in range(T):
    [M, N, K] = map(int, input().split())

    def isMove(y, x):
        return 0 <= y < M and 0 <= x < N

    info = {m : {n : False for n in range(N)} for m in range(M)}
    for _ in range(K):
        [X, Y] = map(int, input().split())
        info[X][Y] = True
    
    count = 0
    for m in range(M):
        for n in range(N):
            if info[m][n]:
                count += 1
                stack = [[m, n]]
                while stack:
                    [y, x] = stack.pop()
                    for [dy, dx] in MOVE:
                        if isMove(y + dy, x + dx) and info[y + dy][x + dx]:
                            info[y + dy][x + dx] = False
                            stack.append([y + dy, x + dx])
    print(count)