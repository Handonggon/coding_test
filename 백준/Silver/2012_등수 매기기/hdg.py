import sys
input = sys.stdin.readline

N = int(input())
info = sorted([int(input()) for n in range(N)])

answer = 0
for i in range(N):
    answer += abs(info[i] - (i + 1))
print(answer)