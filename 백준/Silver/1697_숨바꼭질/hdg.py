import sys
from collections import deque
input = sys.stdin.readline

MOVE = [lambda item: item - 1, lambda item: item + 1, lambda item: item * 2]
[N, K] = map(int, input().split())
INF = 200001

def bfs():
    visited = set()
    queue = deque([[N, 0]])
    visited.add(N)

    while queue:
        [curr, count] = queue.popleft()
        if curr == K:
            return count
        
        for move in MOVE:
            next = move(curr)
            if next <= INF and not next in visited:
                visited.add(next)
                queue.append([next, count + 1])
print(bfs())