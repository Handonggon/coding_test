import sys
input = sys.stdin.readline

INF = 10000
[N, M] = map(int, input().split())
adj = [[0 if v == u else INF for v in range(N)] for u in range(N)]
for _ in range(M):
    [A, B] = map(int, input().split())
    adj[A - 1][B - 1] = 1
    adj[B - 1][A - 1] = 1

for m in range(N):
    for s in range(N):
        for e in range(N):
            adj[s][e] = min(adj[s][e], adj[s][m] + adj[m][e])

answer = 0
minimum = INF
for v in range(N):
    if minimum > sum(adj[v]):
        answer = v + 1
        minimum = sum(adj[v])
print(answer)