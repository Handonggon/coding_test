import sys
input = sys.stdin.readline

[N, M] = [5, 4]
NUMBER = ['0b000010010010000'
        , '0b110110110110110'
        , '0b000110000011000'
        , '0b000110000110000'
        , '0b010010000110110'
        , '0b000011000110000'
        , '0b000011000010000'
        , '0b000001001001001'
        , '0b000010000010000'
        , '0b000010000110000']

info = ['0b' for m in range(M)]
for _ in range(N):
    s = input().strip().split(' ')
    for i in range(M):
        info[i] += s[i]

answer = []
for s in info:
    for [i, number] in enumerate(NUMBER):
        if int(s.replace('#', '1').replace('.', '0'), 2) & int(number, 2) == 0:
            answer.append(i)
            break
print("{0}{1}:{2}{3}".format(*answer))