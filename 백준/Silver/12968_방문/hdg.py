import sys
input = sys.stdin.readline

[R, C, K] = list(map(int, input().split()))
if K == 1:
    print(1)
else:
    if (R * C) % 2 == 0:
        print(1)
    else:
        print(0)