import sys
input = sys.stdin.readline

[N, M] = map(int, input().split())
info = [list(map(int, input().strip())) for _ in range(N)]

prefix = [[0 for m in range(M + 1)] for n in range(N + 1)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        prefix[n][m] = info[n - 1][m - 1] + prefix[n][m - 1] + prefix[n - 1][m] - prefix[n - 1][m - 1]

def subtotal(n1, m1, n2, m2):
    return prefix[n2][m2] - prefix[n2][m1] - prefix[n1][m2] + prefix[n1][m1]

answer = 0
# 1.三
for n1 in range(1, N - 1):
    for n2 in range(n1 + 1, N):
        answer = max(answer, subtotal(0, 0, n1, M) * subtotal(n1, 0, n2, M) * subtotal(n2, 0, N, M))
# 2.|||
for m1 in range(1, M - 1):
    for m2 in range(m1 + 1, M):
        answer = max(answer, subtotal(0, 0, N, m1) * subtotal(0, m1, N, m2) * subtotal(0, m2, N, M))
# 3.ㅓ
for n in range(1, N):
    for m in range(1, M):
        answer = max(answer, subtotal(0, 0, n, m) * subtotal(n, 0, N, m) * subtotal(0, m, N, M))
# 4.ㅏ
for n in range(1, N):
    for m in range(1, M):
        answer = max(answer, subtotal(0, 0, N, m) * subtotal(0, m, n, M) * subtotal(n, m, N, M))
# 5.ㅗ
for n in range(1, N):
    for m in range(1, M):
        answer = max(answer, subtotal(0, 0, n, m) * subtotal(0, m, n, M) * subtotal(n, 0, N, M))
# 6.ㅜ
for n in range(1, N):
    for m in range(1, M):
        answer = max(answer, subtotal(0, 0, n, M) * subtotal(n, 0, N, m) * subtotal(n, m, N, M))

print(answer)