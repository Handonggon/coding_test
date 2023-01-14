from collections import deque
import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))
info = list(map(int, input().split()))

# [N, M] = [32, 6]
# info = [27, 16, 30, 11, 6, 23]
dq = deque([i for i in range(1, N + 1)])

answer = 0
for index in info:
    if dq.index(index) < len(dq) / 2:
        while dq[0] != index:
            dq.append(dq.popleft())
            answer += 1
    else:
        while dq[0] != index:
            dq.appendleft(dq.pop())
            answer += 1
    dq.popleft()
print(answer)