import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
btn = [True for _ in range(10)]
if M > 0:
    for n in map(int, input().split()):
        btn[n] = False

def dfs(curr):
    minimum = 500000
    for num in range(10):
        if btn[num]:
            next = str(num) + curr
            minimum = min(minimum, abs(N - int(next)) + len(next))

            if len(next) < 6:
                minimum = min(minimum, dfs(next))
    return minimum

answer = min(500000, abs(100 - N))
if M < 10:
    answer = min(answer, dfs(""))

print(answer)