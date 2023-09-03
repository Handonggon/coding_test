import sys
import heapq
input = sys.stdin.readline

[F, R] = [0, 1]
INF = 1000 * 100000 + 1
[N, M, X] = map(int, input().split())
adj = [[[] for n in range(N + 1)] for _ in range(2)]
for _ in range(M):
    [v, u, c] = map(int, input().split())
    adj[F][v].append([u, c])
    adj[R][u].append([v, c])

def dijkstra(mod):
    dist = [INF for _ in range(N + 1)]
    queue = []
    heapq.heappush(queue, (0, X))
    dist[X] = 0

    while queue:
        (c, curr) = heapq.heappop(queue)
        if c > dist[curr]:
            continue
        for [next, dc] in adj[mod][curr]:
            if dist[next] > c + dc:
                dist[next] = c + dc
                heapq.heappush(queue, (c + dc, next))
    return dist

answer = -1
for [f, r] in zip(dijkstra(F)[1:], dijkstra(R)[1:]):
    answer = max(answer, f + r)
print(answer)