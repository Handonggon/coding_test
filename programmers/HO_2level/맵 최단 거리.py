from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    def dfs(x,y):
        a = deque()
        a.append((x,y))
        while a:
            x, y = a.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                elif maps[nx][ny] == 0:
                    continue
                elif maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    a.append((nx, ny))
                    
        return maps[n-1][m-1]

    if dfs(0,0) == 0 or dfs(0,0) == 1: return -1
    else: return dfs(0,0)