import sys
input = sys.stdin.readline

[INDEX, VALUE] = [0, 1]

[N, K] = map(int, input().split())
info = list(map(int, input().split()))

answer = [0 for n in range(N)]

order = sorted(enumerate(info), key=lambda item: -item[VALUE])
for index in range(K):
    if index < N:
        answer[order[index][INDEX]] = order[index][INDEX] + 1
        print(order[index][INDEX] + 1)
    else:
        print(0)

for index in answer:
    print(index)