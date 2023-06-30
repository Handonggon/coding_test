import sys
input = sys.stdin.readline
from collections import deque

S1 = input().strip()
S2 = input().strip()

def bfs():
    queue = deque([[0, 0, '']])
    while queue:
        [i1, i2, s] = queue.popleft()
        if i1 == len(S1) and i2 == len(S2):
            return s.replace('*', '')
        
        if i1 < len(S1) and i2 < len(S2) and S1[i1] == S2[i2]:
            queue.append([i1 + 1, i2 + 1, s + S2[i2]])
        if i1 < len(S1) and S1[i1] == '*':
            if i2 < len(S2) : queue.append([i1, i2 + 1, s + S2[i2]])
            queue.append([i1 + 1, i2, s])
        if i2 < len(S2) and S2[i2] == '*':
            if i1 < len(S1) : queue.append([i1 + 1, i2, s + S1[i1]])
            queue.append([i1, i2 + 1, s])
    return -1
print(bfs())