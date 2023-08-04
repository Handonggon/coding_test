import sys
input = sys.stdin.readline

MOVE = [(0, -1), (-1, 0), (0, 1), (1, 0)]
k = int(input())
board = [[False for c in range(5)] for r in range(5)]
tree = 5 * 5
for _ in range(k):
    [y, x] = map(int, input().split())
    board[y - 1][x - 1] = True
    tree -= 1

def dfs(y, x, c):
    if y == 4 and x == 4:
        return all(map(all, board))
    
    answer = 0
    for (dy, dx) in MOVE:
        if 0 <= dy + y < 5 and 0 <= dx + x < 5 and not board[dy + y][dx + x]:
             board[dy + y][dx + x] = True
             answer += dfs(dy + y, dx + x, c + 1)
             board[dy + y][dx + x] = False
    return answer

board[0][0] = True
print(dfs(0, 0, 1))