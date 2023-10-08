import sys
import heapq

[N, K] = map(int, input().split())

MOVE = [lambda loc: (0, loc * 2), lambda loc: (1, loc + 1), lambda loc: (1, loc - 1)]
visited = [False for _ in range(100001)]
visited[N] = True
heap = []
heapq.heappush(heap, (0, N))

answer = -1
while heap:
    (c, curr) = heapq.heappop(heap)
    if curr == K:
        answer = c
        break

    for fn in MOVE :
        (dc, next) = fn(curr)
        if 0 <= next < len(visited):
            if not visited[next]:
                visited[next] = True
                heapq.heappush(heap, (c + dc, next))
print(answer)