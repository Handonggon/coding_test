import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        count += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
    return count