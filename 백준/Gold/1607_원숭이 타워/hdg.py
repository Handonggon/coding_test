N = int(input())

answer = 0
level = 1

while N > 0:
    for _ in range(min(level, N)):
        answer = (answer + pow(2, level-1)) % 9901
        N -= 1
    level += 1

print(answer)