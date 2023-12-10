import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())

nums = list()
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        nums.append(int("".join(map(str, sorted(comb, reverse=True)))))
try:
    print(sorted(nums)[N - 1])
except:
    print(-1)