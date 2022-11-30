import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))
sequence = list(map(int, input().split()))

#[N, M] = [4, 2]
#sequence = [1, 1, 1, 1]

subtotal = [0]
for s in sequence:
    subtotal.append(subtotal[-1] + s)

answer = 0
for i in range(1, N+1):
    for j in range(i):
        if subtotal[i] - subtotal[j] == M:
            answer += 1
            break
print(answer)