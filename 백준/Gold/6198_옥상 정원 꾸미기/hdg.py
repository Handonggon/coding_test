import sys
input = sys.stdin.readline

N = int(input())

stack = []
answer = 0
for _ in range(N):
    n = int(input())
    while stack and stack[-1] <= n:
        stack.pop()
    stack.append(n)

    answer += len(stack) - 1
print(answer)