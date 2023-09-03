import sys
input = sys.stdin.readline

[N, r, c] = map(int, input().split())

def recur(N, r, c):
    if N < 0:
        return 0

    if r < pow(2, N):
        if c < pow(2, N):
            return recur(N - 1, r, c) + (pow(2, N) * pow(2, N) * 0)
        else:
            return recur(N - 1, r, c - pow(2, N)) + (pow(2, N) * pow(2, N) * 1)
    else:
        if c < pow(2, N):
            return recur(N - 1, r - pow(2, N), c) + (pow(2, N) * pow(2, N) * 2)
        else:
            return recur(N - 1, r - pow(2, N), c - pow(2, N)) + (pow(2, N) * pow(2, N) * 3)

print(recur(N - 1, r, c))