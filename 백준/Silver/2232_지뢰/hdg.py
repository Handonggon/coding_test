import sys
input = sys.stdin.readline

N = int(input())
info = [int(input()) for n in range(N)]

# N = 9
# info = [1, 2, 5, 4, 3, 3, 6, 6, 2] # 3, 7, 8

stack = sorted(enumerate(info), key=lambda x: x[1])
isBoom = [False] * N

answer = []
while len(stack) > 0:
    (index, power) = stack.pop()
    if isBoom[index]:
        continue

    isBoom[index] = True
    answer.append(index + 1)

    left = index - 1
    while left >= 0 and info[left + 1] > info[left] and not isBoom[left]:
        isBoom[left] = True
        left -= 1

    right = index + 1
    while right < N and info[right - 1] > info[right] and not isBoom[right]:
        isBoom[right] = True
        right += 1

print(*sorted(answer), sep="\n")