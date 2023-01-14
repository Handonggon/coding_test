import sys
input = sys.stdin.readline

while True:
    N, *info = list(map(int, input().split()))
    info = [0] + info + [0]
    if N == 0:
        break

    stack = []
    answer = 0
    for i in range(len(info)):
        while (stack and info[stack[-1]] > info[i]):
            j = stack.pop()
            answer = max(answer, (i - stack[-1] - 1) * info[j])
        stack.append(i)
    print(answer)