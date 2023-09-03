import sys
import heapq
input = sys.stdin.readline

[N, M] = map(int, input().split())
heap = []
for _ in range(M):
    [A, B, C] = map(int, input().split())
    heapq.heappush(heap, (C, A, B))

parent = [n for n in range(N + 1)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pA = find(a)
    pB = find(b)
    parent[max(pA, pB)] = min(pA, pB)

answer = []
while heap:
    [c, u, v] = heapq.heappop(heap)
    if find(u) == find(v):
        continue
    union(u, v)
    answer.append(c)

print(sum(answer[:-1]))