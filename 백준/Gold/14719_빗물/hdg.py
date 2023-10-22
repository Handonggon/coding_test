import sys
input = sys.stdin.readline

[H, W] = list(map(int, input().split()))
info = list(map(int, input().split()))

answer = 0
for w in range(1, W - 1):
    left = max(info[:w])
    right = max(info[w + 1:])

    h = min(left, right)
    if info[w] < h:
        answer += (h - info[w])
print(answer)