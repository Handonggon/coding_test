import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))
info = sorted(filter(lambda m: m[0] > m[1], [list(map(int, input().split())) for m in range(M)]), key=lambda m: m[0])

city = [-1 for n in range(N+1)]

for [v, w] in info:
    for curr in range(w, v+1):
        city[curr] = city[w] if city[w] > -1 else w

answer = [1]
for div in range(2, N+1):
    if N % div > 0:
        continue

    answer.append(div)

    count = 0
    index = 1
    while index <= N:
        if city[index] == -1:
            count += 1
            index += 1
        else:
            target = city[index]
            while index <= N and city[index] == target:
                count += 1
                index += 1

        if count == N // div:
            count = 0
        elif count > N // div:
            answer.pop()
            break

print(max(answer))