T = int(input())
for _ in range(T):
    [N, M] = list(map(int, input().split()))

    a = []
    for i in range(N):
        a.append(min(i, M))
        M = M - a[i]

    info = {key:[] for key in range(N)}
    for i in range(N):
        info[a[i]].append(i)

    number = 1
    for i in range(N-1, -1, -1):
        for j in info[i]:
            a[j] = number
            number += 1

    print(a)