import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    info = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda p: p[0])

    standard = N
    answer = 0
    for [exam, interview] in info:
        if standard >= interview:
            answer += 1
            standard = interview
    print(answer)