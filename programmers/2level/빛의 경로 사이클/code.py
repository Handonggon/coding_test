MOVE = {'S': [[1, 0, 0], [-1, 0, 1], [0, -1, 2], [0, 1, 3]]
      , 'L': [[0, -1, 2], [0, 1, 3], [1, 0, 0], [-1, 0, 1]]
      , 'R': [[0, 1, 3], [0, -1, 2], [-1, 0, 1], [1, 0, 0]]}

def solution(grid):
    visit = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]
    
    answer = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            for t in range(4): #[U, D, L, R]
                count = 0
                while not (visit[r][c] & pow(2, t)):
                    visit[r][c] += pow(2, t)
                    r = (len(grid) + r + MOVE[grid[r][c]][t][0]) % len(grid)
                    c = (len(grid[r]) + c + MOVE[grid[r][c]][t][1]) % len(grid[r])
                    t = MOVE[grid[r][c]][t][2]
                    count += 1
                answer.append(count)
    return answer