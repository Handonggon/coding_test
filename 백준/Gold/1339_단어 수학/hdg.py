import sys
input = sys.stdin.readline

N = int(input())
info = [list(input().strip()) for _ in range(N)]
maps = {}
for s in info:
    for i in range(len(s)):
        maps[s[i]] = (maps[s[i]] if s[i] in maps else 0) + pow(10, len(s) - i - 1)

answer = 0
number = 9
for v in sorted(list(maps.values()), reverse=True):
    answer += number * v
    number -= 1
print(answer)