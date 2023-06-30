import sys
input = sys.stdin.readline
from collections import deque

[TYPE, C] = [0, 1]
left = deque(input().strip())
right = deque([])
N = int(input())
for _ in range(N):
    info = input().split()
    if info[TYPE] == 'L':
        if left: right.appendleft(left.pop())
    elif info[TYPE] == 'D':
        if right: left.append(right.popleft())
    elif info[TYPE] == 'B':
        if left: left.pop()
    elif info[TYPE] == 'P':
        left.append(info[C])
print("".join(left + right))