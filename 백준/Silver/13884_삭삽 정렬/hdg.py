import math
import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    [K, N] = list(map(int, input().split()))
    info = []
    for n in range(math.ceil(N / 10)):
        info += list(map(int, input().split()))

    stack = sorted(info, key=lambda item: -item)
    for number in info:
        if number == stack[-1]:
            stack.pop()
    print(K, len(stack))