import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

[n, m] = list(map(int, input().split()))
info = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
for i in range(1, n):
    adj[info[i]].append(i + 1)
praise = [0 for _ in range(n + 1)]
for _ in range(m):
    [i, w] = list(map(int, input().split()))
    praise[i] += w

def dfs(curr):
    for next in adj[curr]:
        praise[next] += praise[curr]
        dfs(next)

dfs(1)
print(*praise[1:])