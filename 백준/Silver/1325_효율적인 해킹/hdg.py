import sys
input = sys.stdin.readline
from collections import deque

[N, M] = map(int, input().split())
adj = [[] for y in range(N + 1)]
for _ in range(M):
    [u, v] = map(int, input().split())
    adj[v].append(u)

def getCount(start):
    count = 1
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        for next in adj[curr]:
            if visited[next]:
                continue
            visited[next] = True
            queue.append(next)
            count += 1
    return count

count = [0 for _ in range(N + 1)]
for node in range(1, N + 1):
    count[node] = getCount(node)

answer = []
maximum = max(count)
for node in range(1, N + 1):
    if count[node] == maximum:
        answer.append(node)
print(*answer)