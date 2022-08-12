from collections import deque

DIRECTION = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    isBound = lambda y, x: (y>=0 and y < n and x>=0 and x < m)
    
    queue = deque()
    queue.append([0, 0, 1])
    
    while queue:
        [y, x, dist] = queue.popleft()
        if y == n-1 and x == m-1:
            return dist;
        for (dy, dx) in DIRECTION:
            if isBound(y+dy, x+dx):
                if maps[y+dy][x+dx] == 1 or maps[y+dy][x+dx] > dist+1:
                    maps[y+dy][x+dx] = dist + 1
                    queue.append([y+dy, x+dx, dist+1])
    return -1