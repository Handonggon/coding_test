import sys
input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    [s, e] = map(int, input().split())
    info.append([s, 1])
    info.append([e, -1])
info.sort(key = lambda item: (item[0], item[1]))

answer = 0
count = 0
for i, type in info:
    count += type
    answer = max(answer, count)
print(answer)