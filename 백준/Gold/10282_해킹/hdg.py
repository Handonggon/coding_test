import sys
input = sys.stdin.readline
import heapq

INF = 100000 * 100000 + 1
t = int(input())
for _ in range(t):
    [n, d, c] = list(map(int, input().split()))
    dist = [INF for _ in range(n + 1)]
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        [a, b, s] = list(map(int, input().split()))
        adj[b].append([a, s])

    queue = []
    heapq.heappush(queue, (0, c))
    dist[c] = 0
    while queue:
        [cost, curr] = heapq.heappop(queue)
        if dist[curr] < cost:
            continue
        for [next, c] in adj[curr]:
            if cost + c < dist[next]:
                dist[next] = cost + c
                heapq.heappush(queue, (cost + c, next))

    answer = list(filter(lambda item: item < INF, dist))
    print(len(answer), max(answer))