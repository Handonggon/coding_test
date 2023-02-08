import heapq
import sys
input = sys.stdin.readline

N = int(input())
info = sorted([list(map(int, input().split())) for _ in range(N)], key= lambda item: item[0])

pq = []
for [deadline, count] in info:
    heapq.heappush(pq, count)
    if len(pq) > deadline:
        heapq.heappop(pq)
print(sum(pq))