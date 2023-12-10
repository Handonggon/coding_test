import sys
input = sys.stdin.readline

N = int(input())
seq = []
friend = [[] for _ in range(N + 1)]

for _ in range(N ** 2):
    [me, *info] = map(int, input().split())
    seq.append(me)
    friend[me] = info

    