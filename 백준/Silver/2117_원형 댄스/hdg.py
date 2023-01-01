import sys
input = sys.stdin.readline

n = int(input())

answer = 0
up = 1
for index in range(3, n + 1):
    answer += up
    if index % 2 == 0:
        up += 1
print(answer)