import sys
import math
from collections import deque
input = sys.stdin.readline

DIRE = {'+': 1, '-': -1}
N = int(input())
info = [0]
for _ in range(N):
    [num, dire] = input().split()
    info.append(int(num) * DIRE[dire])

def reverse(array, s, e):
    for i in range(math.ceil((e - s) / 2)):
        array[s + i], array[e - i] = array[e - i], array[s + i]
    for i in range(s, e + 1):
        array[i] *= -1
    return array

def bfs():
    queue = deque([[info.copy(), 0]])
    visited = set()

    while queue:
        [cake, count] = queue.popleft()

        isSuccess = True
        for index in range(N + 1):
            if index != cake[index]:
                isSuccess = False
                break
        if isSuccess:
            return count

        for index in range(1, N + 1):
            cake = reverse(cake, 1, index)
            
            if not ''.join(map(str, cake)) in visited:
                queue.append([cake.copy(), count + 1])
                visited.add(''.join(map(str, cake)))

            cake = reverse(cake, 1, index)
    return -1

print(bfs())