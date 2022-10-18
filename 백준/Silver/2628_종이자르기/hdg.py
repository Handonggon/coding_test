[C, R] = list(map(int, input().split()))
N = int(input())
info = sorted([list(map(int, input().split())) for _ in  range(N)], key=lambda item: item[1]) + [[0, R], [1, C]]

start = [0, 0]
answer = [0, 0]

for [type, end] in info:
    answer[type] = max(answer[type], end - start[type])
    start[type] = end

print(answer[0] * answer[1])