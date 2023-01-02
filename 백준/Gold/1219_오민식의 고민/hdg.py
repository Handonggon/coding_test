import sys
input = sys.stdin.readline

[N, S, D, M] = list(map(int, input().split()))
edges = [list(map(int, input().split())) for m in range(M)]
maximum = list(map(int, input().split()))

# [N, S, D, M] = [5, 0, 4, 7]
# edges = [[0, 1, 13], [1, 2, 17], [2, 4, 20], [0, 3, 22], [1, 3, 4747], [2, 0, 10], [3, 4, 10]]
# maximum = [0, 0, 0, 0, 0]

INF = N * -1000000
GEE = N * 1000000

dist = [INF] * N

dist[S] = maximum[S]
for n in range(2 * N):
    for m in range(M):
        [curr, next, cost] = edges[m]
        cost = maximum[next] - cost
        if dist[curr] == INF:
            continue
        if dist[curr] == GEE:
            dist[next] = GEE
            continue
        if dist[curr] + cost > dist[next]:
            dist[next] = dist[curr] + cost
            if n >= N - 1:
                dist[next] = GEE

if dist[D] == INF:
    print("gg")
elif dist[D] == GEE:
    print("Gee")
else:
    print(dist[D])