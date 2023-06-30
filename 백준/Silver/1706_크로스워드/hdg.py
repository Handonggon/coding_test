import sys
input = sys.stdin.readline

[R, C] = map(int, input().split())
info = [list(input().strip()) for _ in range(R)]


answer = []
for r in range(R):
    word = ''
    for c in range(C):
        if info[r][c] == '#':
            answer.append(word)
            word = ''
        else:
            word += info[r][c]
    answer.append(word)

for c in range(C):
    word = ''
    for r in range(R):
        if info[r][c] == '#':
            answer.append(word)
            word = ''
        else:
            word += info[r][c]
    answer.append(word)

print(sorted(filter(lambda item: len(item) > 1, answer))[0])