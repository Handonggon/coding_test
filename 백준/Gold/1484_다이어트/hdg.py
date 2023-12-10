import sys
input = sys.stdin.readline

G = int(input())

[left, right] = [1, 1]
answer = []
while True:
    diff = pow(right, 2) - pow(left, 2)
    if diff == G:
        answer.append(right)
    if diff > G:
        if right - left == 1:
            break
        left += 1
    else:
        right += 1

if answer:
    print(*answer, sep="\n")
else:
    print(-1)