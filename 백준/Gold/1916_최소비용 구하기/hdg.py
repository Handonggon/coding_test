import sys
import heapq
input = sys.stdin.readline

INF = 1000 * 100000 + 1
N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    [v, u, c] = map(int, input().split())
    adj[v].append([u, c])
[S, E] = map(int, input().split())

dist = [INF for _ in range(N + 1)]
queue = []
heapq.heappush(queue, (0, S))
dist[S] = 0

while queue:
    (c, curr) = heapq.heappop(queue)
    if c > dist[curr]:
        continue
    for [next, dc] in adj[curr]:
        if dist[next] > c + dc:
            dist[next] = c + dc
            heapq.heappush(queue, (c + dc, next))
print(dist[E])