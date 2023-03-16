from collections import deque
MOVE = [[1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r'], [-1, 0, 'u']]

def solution(n, m, x, y, r, c, k):
    isMove = lambda x, y: 1 <= x <= n and 1 <= y <= m
    getDist = lambda x, y: abs(r - x) + abs(c - y)
    queue = deque([[x, y, ""]])
    
    while queue:
        [x, y, t] = queue.popleft()
        if (x, y) == (r, c) and (k - len(t)) % 2 == 1:
            return "impossible"
        if (x, y) == (r, c) and len(t) == k:
            return t
        
        for [dx, dy, dt] in MOVE:
            if isMove(x + dx, y + dy) and getDist(x + dx, y + dy) + len(t) + 1 <= k:
                queue.append([x + dx, y + dy, t + dt])
                break
    
    return "impossible"