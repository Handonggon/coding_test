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

    print(*a, sep=' ')

#############################################
    
    cnt = 0
    for j in range(1, N):
        x = a[j]
        i = j - 1
        while i >= 0 and a[i] > x:
            cnt = cnt + 1
            a[i+1] = a[i]
            i = i-1
        a[i+1] = x
        
    print(cnt)