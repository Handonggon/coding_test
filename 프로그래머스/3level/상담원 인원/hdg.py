import heapq
import itertools

def solution(k, n, reqs):
    cases = set()
    for product in itertools.product(range(1, n + 1), repeat = k):
        if sum(product) == n:
            cases.add(product)

    typeByPerson = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    for type in range(1, k + 1):
        for person in range(1, n + 1):
            heap = []
            for [start, duration, _] in filter(lambda x: x[2] == type, reqs):
                while heap and heap[0] < start:
                    heapq.heappop(heap)
                if len(heap) < person:
                    heapq.heappush(heap, start + duration)
                else:
                    time = heapq.heappop(heap)
                    heapq.heappush(heap, time + duration)
                    typeByPerson[type][person] += time - start
    answer = 10 ** 9
    for case in cases:
        total = 0
        for type in range(1, k + 1):
            total += typeByPerson[type][case[type - 1]]
        answer = min(answer, total)
    return answer