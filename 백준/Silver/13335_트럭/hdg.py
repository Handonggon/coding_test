import sys
from collections import deque
input = sys.stdin.readline

[n, w, L] = map(int, input().split())
a = deque(map(int, input().split()))

T = 0
total = 0
queue = deque([0 for _ in range(w)])
while queue:
    total -= queue.popleft()
    if a:
        if total + a[0] > L:
            queue.append(0)
        else:
            total += a[0]
            queue.append(a.popleft())
    T += 1
print(T)