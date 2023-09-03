import sys
input = sys.stdin.readline

V = int(input())
adj = [[] for _ in range(V + 1)]
for _ in range(V):
    [v, *node] = map(int, input().split())
    for i in range(0, len(node), 2):
        if node[i] == -1:
            break
        adj[v].append([node[i], node[i + 1]])

def dfs(x, y):
    for a, b in adj[x]:
        if visited[a] == -1:
            visited[a] = b + y
            dfs(a, b + y)

visited = [-1 for _ in range(V + 1)]
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1 for _ in range(V + 1)]
visited[start] = 0
dfs(start, 0)

print(max(visited))