from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
[s, d] = list(map(int, input().split()))
info = [[] for _ in range(n + 1)]
m = int(input())
for _ in range(m):
    [x, y] = list(map(int, input().split()))
    info[x].append(y)
    info[y].append(x)

visited = [False for _ in range(n + 1)]
queue = deque([[s, 0]])
answer = -1
while queue:
    [curr, count] = queue.popleft()
    visited[curr] = True

    if d == curr:
        answer = count

    for next in info[curr]:
        if not visited[next]:
            queue.append([next, count + 1])
print(answer)