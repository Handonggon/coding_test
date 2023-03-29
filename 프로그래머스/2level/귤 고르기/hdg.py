from collections import Counter
import heapq

def solution(k, tangerine):
    tangerine = Counter(tangerine)
    heap = []
    for item in tangerine.values():
        heapq.heappush(heap, -item)
    
    total = 0
    while heap:
        total -= heapq.heappop(heap)
        if total >= k:
            break
    return len(tangerine) - len(heap)