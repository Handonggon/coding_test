import heapq

N = int(input())
info = sorted([list(map(int ,input().split())) for _ in range(N)], key=lambda info: info[0])
[L, P] = list(map(int ,input().split()))

heap = []

curr = -1
answer = 0
ispossible = True
while P < L:
    for next in range(curr+1, N):
        [dist, fuel] = info[next]
        if dist > P:
            break
        heapq.heappush(heap, -fuel)
        curr = next
   
    if len(heap) == 0:
        ispossible = False
        break

    P += -heapq.heappop(heap)
    answer += 1

print(answer) if ispossible else print(-1)