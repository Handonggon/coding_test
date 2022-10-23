N = int(input())
info = [int(input()) for _ in range(N)]

[left, right] = [0, 0]
answer = [0, 0]
for index in range(N):
    if info[index] > left:
        answer[0] += 1
        left = info[index]

    if info[N-1-index] > right:
        answer[1] += 1
        right = info[N-1-index]

for data in answer:
    print(data)