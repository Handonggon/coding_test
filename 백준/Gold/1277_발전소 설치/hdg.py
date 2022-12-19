import sys
import math
import heapq
input = sys.stdin.readline

[N, W] = list(map(int, input().split()))
M = float(input())
plant = [list(map(int, input().split())) for n in range(N)]
wire = [list(map(int, input().split())) for n in range(W)]

# [N, W] = [9, 3]
# M = 2.0
# plant = [[0, 0], [0, 1], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [4, 1], [4, 3]]
# wire = [[1, 2], [2, 3], [3, 4]]

graph = [[200000.0 for x in range(N + 1)] for y in range(N + 1)]
for i in range(N):
    for j in range(i, N):
        dist = math.sqrt(pow(plant[i][0] - plant[j][0], 2) + pow(plant[i][1] - plant[j][1], 2))
        if M >= dist:
            graph[i + 1][j + 1] = dist
            graph[j + 1][i + 1] = dist

for [y, x] in wire:
    graph[y][x] = 0.0
    graph[x][y] = 0.0

distance = [200000.0] * (N + 1)

start = 1
pq = []
heapq.heappush(pq, (0, start))
distance[start] = 0

while pq:
    [dist, curr] = heapq.heappop(pq)
    if dist > distance[curr]:
        continue

    for next in range(1, N + 1):
        cost = dist + graph[curr][next]
        if graph[curr][next] <= M and distance[next] > cost:
            distance[next] = cost
            heapq.heappush(pq, (cost, next))

print(math.floor(distance[N] * 1000))