import sys
input = sys.stdin.readline

N = int(input())
L = int(input())
C = int(input())

# N = 7
# L = 2
# C = 6

answer = N
for count in range(1, min(((C - L) // (L + 1)) + 1, N) + 1):
    if count % 13 == 0:
        continue
    remain = N % count

    add = 0
    if remain > 0:
        if remain % 13 == 0 and remain + 1 == count:
            add = 2
        else:
            add = 1
    answer = min(answer, N // count + add)
print(answer)