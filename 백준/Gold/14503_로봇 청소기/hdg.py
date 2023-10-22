import sys
input = sys.stdin.readline

MOVE = [[-1, 0], [0, 1], [1, 0], [0, -1]]
[N, M] = list(map(int, input().split()))
[r, c, d] = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
clean = [[False for _ in range(M)] for _ in range(N)]

def isMove(y, x):
    return 0 <= y < N and 0 <= x < M and board[y][x] == 0

answer = 0
while True:
    # 1.현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not clean[r][c]:
        answer += 1
        clean[r][c] = True
    else:
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        isContinue = False
        for i in range(1, len(MOVE) + 1):
            [dr, dc] = MOVE[(len(MOVE) + d - i) % len(MOVE)]
            if isMove(r + dr, c + dc) and not clean[r + dr][c + dc]:
                [r, c, d] = [r + dr, c + dc, (len(MOVE) + d - i) % len(MOVE)]
                isContinue = True
                break
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if not isContinue:
            [dr, dc] = MOVE[(len(MOVE) + d - 2) % len(MOVE)]
            if isMove(r + dr, c + dc):
                [r, c] = [r + dr, c + dc]
            else:
                break
print(answer)