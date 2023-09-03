import sys
input = sys.stdin.readline

INF = (500 * 10000) + 1
TC = int(input())
for _ in range(TC):
    [N, M, W] = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        [S, E, T] = map(int, input().split())
        adj[S].append([E, T])
        adj[E].append([S, T])

    for _ in range(W):
        [S, E, T] = map(int, input().split())
        adj[S].append([E, -T])

    def timeTravel():
        dist = [INF for _ in range(N + 1)]
        dist[1] = 0

        for i in range(0, N + 1):
            for curr in range(0, N + 1):
                for [next, cost] in adj[curr]:
                    dist[next] = min(dist[next], dist[curr] + cost)
        
        for curr in range(0, N + 1):
            for [next, cost] in adj[curr]:
                if dist[next] > dist[curr] + cost:
                    return True
        return False
    
    print("YES" if timeTravel() else "NO")