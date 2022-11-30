import sys
input = sys.stdin.readline

[N, W, B] = list(map(int, input().split()))
box = [-1 for w in range(W)] 

def isPossible(b, board):
    for h in range(len(board)):
        for w in range(W):
            if board[h][w] == 'X' and box[w] >= b + h:
                return False
    return True

answer = []
for n in range(N):
    H = int(input())
    board = [input().strip() for n in range(H)][::-1]

    start = 0
    for b in range(B-H+1):
        if isPossible(b, board):
            start = b
            break
    
    if start == 0:
        box = [-1 for w in range(W)]

    for h in range(H):
        for w in range(W):
            if board[h][w] == 'X':
                box[w] = max(box[w], start + h)

    if start > 0:
        answer.pop()
    answer.append(max(box)+1)

print(*answer)