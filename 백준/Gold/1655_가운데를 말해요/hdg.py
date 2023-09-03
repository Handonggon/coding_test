import sys
import heapq
input = sys.stdin.readline

maximum = [100000]
minimum = [100000]

N = int(input())
for n in range(N):
    num = int(input())
    if len(minimum) == len(maximum):
        heapq.heappush(maximum, -num)
    else:
        heapq.heappush(minimum, num)
    if -maximum[0] > minimum[0]:
        heapq.heappush(maximum, -heapq.heappop(minimum))
        heapq.heappush(minimum, -heapq.heappop(maximum))

    print(-maximum[0])