import sys
input = sys.stdin.readline

[N, K] = map(int, input().split())
answer = 0
while bin(N).count('1') > K:
    N = N + 1
    answer = answer + 1
print(answer)