import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))
info = {v: [] for v in range(1, N+1)}
for m in range(M):
    [v, w] = list(map(int, input().split()))
    info[v].append(w)

fenwick = [0 for n in range(N+1)]

def update(i, v):
    while i <= N:
        fenwick[i] += v
        i += i & -i

def query(i):
    ret = 0
    while i > 0:
        ret += fenwick[i]
        i -= i & -i
    return ret

answer = 0
for v in info:
    for w in sorted(info[v]):
        answer += query(N) - query(w)
        update(w, 1)
print(answer)