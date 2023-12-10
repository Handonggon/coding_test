import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for u in range(N):
    s = input()
    for v in range(N):
        if(s[v].isalpha()):
            if(s[v].islower()):
                heapq.heappush(heap, (ord(s[v]) - ord('a') + 1, u + 1, v + 1))
            else:
                heapq.heappush(heap, (ord(s[v]) - ord('A') + 27, u + 1, v + 1))
parent = [n for n in range(N + 1)]
def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    pX = find(x)
    pY = find(y)

    parent[pX] = min(pX, pY)
    parent[pY] = min(pX, pY)

answer = 0
while heap:
    (cost, u, v) = heapq.heappop(heap)
    if find(u) == find(v):
        answer += cost
    else:
        union(u, v)

print(answer) if all(find(node) == 1 for node in parent[1:]) else print(-1)