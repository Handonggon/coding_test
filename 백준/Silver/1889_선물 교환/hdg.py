from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(lambda item: int(item) - 1, input().split())) for _ in range(N)]

dp = [0 for n in range(N)]

for [p1, p2] in info:
    dp[p1] += 1
    dp[p2] += 1

queue = deque(list(map(lambda item: item[0], filter(lambda item: item[1] < 2, enumerate(dp)))))

visited = [False for n in range(N)]
while queue:
    index = queue.popleft()
    if visited[index]:
        continue
    visited[index] = True
    
    [p1, p2] = info[index]
    
    dp[p1] -= 1
    if dp[p1] < 2:
        queue.append(p1)
    dp[p2] -= 1
    if dp[p2] < 2:
        queue.append(p2)

answer = list(map(lambda item: item[0] + 1, filter(lambda item: not item[1], enumerate(visited))))
print(len(answer))
if answer:
    print(*answer)