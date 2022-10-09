[N, K] = list(map(int, input().split()))

photo = [list(map(int, input().split())) for _ in range(N)]

for row in range(N * K):
    for col in range(N * K):
        print(photo[row // K][col // K], end=' ')
    print()