import sys
input = sys.stdin.readline
'''
[N, M] = list(map(int, input().split()))
info = [[0 for m in range(M+1)]] + [[0] + list(map(int, input().split())) for n in range(N)]

answer = -10000 * N * M
for n2 in range(1, N+1):
    for m2 in range(1, M+1):
        info[n2][m2] = info[n2][m2] + info[n2-1][m2] + info[n2][m2-1] - info[n2-1][m2-1]
        for n1 in range(n2):
            for m1 in range(m2):
                answer = max(answer, info[n2][m2] - info[n2][m1] - info[n1][m2] + info[n1][m1])
print(answer)
'''
[N, M] = list(map(int, input().split()))
info = [list(map(int, input().split())) for n in range(N)]

#[N, M] = [3, 5]
#info = [[2, 3, -21, -22, -23], [5, 6, -22, -23, -25], [-22, -23, 4, 10, 2]]

answer = -10000 * N * M
for i in range(N):
    p = [0] * M
    for j in range(i, N):
        t = [0] * M
        for k in range(M):
            p[k] += info[j][k]
            t[k] += max(t[k-1] + p[k], p[k])
            answer = max(answer, t[k])
print(answer)