import sys
import math
input = sys.stdin.readline

k = int(input())
answer = []
for div in range(2, math.ceil(math.sqrt(k)) + 1):
    while k % div == 0:
        answer.append(div)
        k = k // div
if k > 1:
    answer.append(k)
print(len(answer))
print(*answer)