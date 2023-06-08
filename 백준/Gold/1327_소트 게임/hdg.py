from collections import deque
import sys
input = sys.stdin.readline

[N, K] = map(int, input().split())
info = list(input().split())
answer = ''.join(map(str, range(1, N + 1)))

def bfs():
    queue = deque([[''.join(info), 0]])
    visited = set()
    while queue:
        [curr, count] = queue.popleft()
        if curr == answer:
            return count
        for i in range(N - K + 1):
            next = curr[:i] + curr[i:i+K][::-1] + curr[i+K:]
            if next in visited:
                continue
            visited.add(next)
            queue.append([next, count + 1])
    return -1

print(bfs())