import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split(" ")))
if max(info) > 50:
    print(0)
else:
    answer = 0
    for unit in list(permutations(info)):
        percent = [False for i in range(101)]
        i = 0
        for j in unit:
            i += j
            percent[i] = True
        count = 0
        for i in range(0, 51):
            count += (percent[i] and percent[i + 50])
        answer = max(answer, count)
    print(answer)