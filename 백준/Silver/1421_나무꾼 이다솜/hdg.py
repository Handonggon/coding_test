import sys
input = sys.stdin.readline

[N, C, W] = map(int, input().split())
trees = [int(input()) for _ in range(N)]

answer = 0
for standard in range(1, max(trees) + 1):
    money = 0
    for tree in trees:
        count, remain = divmod(tree, standard)
        if count == 0:
            continue
        money += max(W * standard * count - (C * (count - 1) if remain == 0 else C * count), 0)
    answer = max(money, answer)
print(answer)