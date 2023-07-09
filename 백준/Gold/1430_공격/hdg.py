import sys
import math
input = sys.stdin.readline

[N, R, D, X, Y] = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

def getDistance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

adj = [[] for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if getDistance(*info[i], *info[j]) <= R:
            adj[i].append(j)
            adj[j].append(i)

stack = []
costs = [N + 1 for _ in range(N)]
for node in range(N):
    if getDistance(X, Y, *info[node]) <= R:
        stack.append([node, 1])

while stack:
    [curr, cost] = stack.pop()
    if cost >= costs[curr]:
        continue
    costs[curr] = cost
    for next in adj[curr]:
        stack.append([next, cost + 1])

answer = 0
for cost in costs:
    if cost == N + 1:
        continue
    answer += D / pow(2, cost - 1)
print(answer)