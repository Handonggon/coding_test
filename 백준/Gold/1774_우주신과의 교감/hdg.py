import sys
import math
input = sys.stdin.readline

[X, Y] = [0, 1]
[U, V, COST] = [0, 1, 2]
[N, M] = map(int, input().split())
loc = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]

nodes = []
for i in range(N - 1):
    for j in range(i + 1, N):
        nodes.append([i + 1, j + 1, math.sqrt(pow((loc[i][X] - loc[j][X]), 2) + pow((loc[i][Y] - loc[j][Y]), 2))])

nodes = sorted(nodes, key = lambda item: (item[COST]))

parent = [i for i in range(N + 1)]
def find(a):
    if a == parent[a]:
        return a;
    return find(parent[a])

def union(a, b):
    Pa = find(a)
    Pb = find(b)
    if Pa < Pb : parent[Pb] = Pa
    else : parent[Pa] = Pb

for [u, v] in info:
    union(u, v)

answer = 0.0
for [u, v, cost] in nodes:
    if find(u) == find(v):
        continue
    union(u, v)
    answer += cost

print("{:.2f}".format(round(answer, 2)))