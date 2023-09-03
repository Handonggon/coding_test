import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
MAX = N + 1
prime = [False, False] + [True] * (MAX-1)
for i in range(2, MAX + 1):
  if prime[i]:
    for j in range(2 * i, MAX + 1, i):
        prime[j] = False

answer = 0
dequeue = deque([])
summary = 0
for num in range(1, N + 1):
    if(prime[num]):
        dequeue.append(num)
        summary += num

        while summary > N:
            summary -= dequeue.popleft()
        
        if summary == N:
            answer += 1
print(answer)