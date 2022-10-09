T = int(input())

for _ in range(T):
    N = int(input())
    info = [tuple(input().split()) for _ in range(N)]

    credit, total = 0, 0
    for (C, G) in info:
        credit += int(C)
        total += int(C) * float(G)

    print(credit, round(total / credit, 1))