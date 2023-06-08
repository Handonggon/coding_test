import sys
input = sys.stdin.readline

[N, M] = map(int, input().split())
info = []
for _ in range(N):
    [name, yn] = input().split()
    info.append(int('0b' + ''.join(map(lambda c: str(int(c == 'Y')), list(yn))), 2))

answer = [[-1, 0]]
stack = [[0, 0, 0]]

while stack:
    [curr, count, state] = stack.pop()
    if curr == N:
        answer.append([count, state])
        continue
    stack.append([curr + 1, count, state])
    stack.append([curr + 1, count + 1, state | info[curr]])

[count, state] = sorted(answer, key=lambda item: (item[1], -item[0])).pop()
print(count)