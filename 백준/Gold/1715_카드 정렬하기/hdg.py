import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

answer = 0
if N > 1:
    for n in range(N - 1):
        sum = heapq.heappop(heap) + heapq.heappop(heap)
        answer += sum
        heapq.heappush(heap, sum)

print(answer)