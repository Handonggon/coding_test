import sys
input = sys.stdin.readline

[N, P] = list(map(int, input().split()))
info = sorted([list(map(int, input().split())) for n in range(N)], key= lambda item: (item[1], -item[0])) 

# [N, P] = [3, 100]
# info = sorted([[1, 1], [1, 2], [1, 3]], key= lambda item: (item[1], -item[0])) #97.06

# [N, P] = [10, 1000000000]
# info = [[10, 2], [2, 3], [6, 2], [3, 2], [3, 1], [2, 3], [9, 3], [4, 3], [2, 3], [10, 1]] #7.921497975738132E8

items = {1: [], 2:[], 3:[]}
for [c, p] in info:
    items[p].append(c)

for p in items:
    items[p].sort()

answer = P
for i in range(len(items[1])+1):
    I = sum(items[1][:i])
    for j in range(len(items[2])+1):
        J = sum(items[2][:j])
        for k in range(len(items[3])+1):
            K = sum(items[3][:k])
            answer = min(answer, (P * pow(0.99, i) * pow(0.98, j) * pow(0.97, k)) + I + J + K)
print(answer)