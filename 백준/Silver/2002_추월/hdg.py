import sys
input = sys.stdin.readline

N = int(input())

entr = [input().rstrip() for _ in range(N)]
exit = {input().rstrip(): index for index in range(N)}

loc = 0
answer = 0
for car in entr:
    if exit[car] >= loc:
        loc = exit[car]
    else:
        answer += 1
print(answer)