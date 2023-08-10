import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    [n, *info] = map(int, input().split())
    if n == 0:
        break
    
    for select in combinations(info, 6):
        print(*select)
    print()