import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    info = []
    info = sorted([input().strip() for _ in range(n)])

    answer = False
    for i in range(1, n):
        answer = answer or info[i].startswith(info[i - 1])
    
    print("NO") if answer else print("YES")