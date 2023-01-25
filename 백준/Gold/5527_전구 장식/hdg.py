import sys
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))

chain = [0, 0]

count = 1
for index in range(1, N):
    if info[index] == info[index - 1]:
        chain.append(count)
        count = 1
    else:
        count += 1
chain.append(count)

answer = 0
for index in range(len(chain) - 2):
    answer = max(answer, chain[index] + chain[index + 1] + chain[index + 2])
print(answer)