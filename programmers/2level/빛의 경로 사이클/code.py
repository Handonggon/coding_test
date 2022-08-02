STATE = {'S': 0, 'L': 1, 'R': -1}
MOVE = [(-1, 0), (0, 1), (1, 0), (0, -1)] #[U, L, D, R]

def solution(grid):
    [H, W, M] = [len(grid), len(grid[0]), len(MOVE)]
    visit = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]
    
    answer = []
    for r in range(H):
        for c in range(W):
            for m in range(M):
                count = 0
                while not (visit[r][c] & pow(2, m)):
                    visit[r][c] += pow(2, m)
                    [r, c] = [(r + MOVE[m][0]) % H, (c + MOVE[m][1]) % W]
                    m = (m + STATE[grid[r][c]]) % M
                    count += 1
                if(count):
                    answer.append(count)
    return sorted(answer)
