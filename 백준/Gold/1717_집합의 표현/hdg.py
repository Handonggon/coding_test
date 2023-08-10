import sys
input = sys.stdin.readline

[SUM, CHECK] = [0, 1]
[n, m] = map(int, input().split())
parents = [i for i in range(n + 1)]

def find(a):
    if parents[a] == a:
        return a
    return find(parents[a])

def union(a, b):
    pA = find(a)
    pB = find(b)
    parents[min(pA, pB)] = max(pA, pB)

for _ in range(m):
    [mode, a, b] = map(int, input().split())
    if mode == SUM:
        union(a, b)
    if mode == CHECK:
        print("YES" if find(a) == find(b) else "NO")