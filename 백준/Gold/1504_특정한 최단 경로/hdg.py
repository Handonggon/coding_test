import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize
[N, E] = map(int, input().split())
adj = [[0 if a == b else INF for b in range(N + 1)] for a in range(N + 1)]
for _ in range(E):
    [a, b, c] = map(int, input().split())
    adj[a][b] = adj[b][a] = c
[v1, v2] = map(int, input().split())

def dijkstra(start, end):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, curr = heapq.heappop(q)
        if dist > distance[curr]:
            continue

        for next in range(N + 1):
            cost = dist + adj[curr][next]
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance[end]

answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
print(answer if answer < INF else -1)