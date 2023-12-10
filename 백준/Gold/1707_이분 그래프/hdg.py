import sys
input = sys.stdin.readline
from collections import deque

[RED, BLUE] = [-1, 1]

K = int(input())
for _ in range(K):
    [V, E] = map(int, input().split())
    info = [[] for v in range(V + 1)]
    for e in range(E):
        [u, v] = map(int, input().split())
        info[u].append(v)
        info[v].append(u)

    colors = [0 for v in range(V + 1)]
    for v in range(1, V + 1):
        if colors[v] == 0:
            colors[v] = RED
            queue = deque([[v, RED]])
            while queue:
                [curr, color] = queue.popleft()

                for next in info[curr]:
                    if colors[next] == 0:
                        colors[next] = color * -1
                        queue.append([next, color * -1])

    isBipartiteGraph = True
    for v in range(1, V + 1):
        for u in info[v]:
            if colors[v] == colors[u]:
                isBipartiteGraph = False
    
    if isBipartiteGraph:
        print("YES")
    else:
        print("NO")