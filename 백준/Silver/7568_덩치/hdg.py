import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for n in range(N)]

for i in range(N):
    rank = 1
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            rank += 1
    print(rank, end=' ')