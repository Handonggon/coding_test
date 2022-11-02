[N, M, K] = list(map(int, input().split()))
info = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: -x[0])

answer = 0
for [score, count] in info:
    if K > 0:
        answer += score * min(count, K)
        K -= count;
    else:
        break;

print(answer)