import sys
input = sys.stdin.readline

N = int(input())
info = {}
for _ in range(N):
    key = input().strip()
    info[key] = ((info[key] + 1) if key in info else 1)
print(sorted(info.keys(), key= lambda item : (-info[item], item))[0])