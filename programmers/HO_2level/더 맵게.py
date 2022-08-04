def solution(scoville, K):
    import heapq   
    result = 0   
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) >= 2:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)

            c = a + 2*b

            heapq.heappush(scoville, c)
            result += 1
        else:
            break

    if sum(scoville) < K: return -1
    elif result == 0: return -1
    else: return result