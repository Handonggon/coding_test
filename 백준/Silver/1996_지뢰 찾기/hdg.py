MOVE = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

N = int(input())
map = [list(input()) for _ in range(N)]
def isBoom(r, c):
    return r >= 0 and r < N and c >= 0 and c < N and map[r][c].isdigit()

for row in range(N):
    for col in range(N):
        if map[row][col] == '.':
            answer = 0
            for move in MOVE:
                [dr, dc] = move
                if isBoom(row+dr, col+dc):
                    answer += int(map[row+dr][col+dc])
            print('M', end='') if answer >= 10 else print(answer, end='')
        else:
            print('*', end='')
    print()