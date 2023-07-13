import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = int(input())
    for div in range(2, num + 1):
        if num < 2: break
        count = 0
        while num % div == 0:
            count += 1
            num = num // div
        if count > 0: print(div, count)