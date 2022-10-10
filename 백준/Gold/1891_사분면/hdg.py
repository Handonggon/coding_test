BIN = ['', '00', '01', '11', '10']

[d, number] = list(map(int, input().split()))
[dx, dy] = list(map(int, input().split()))

y, x = map(lambda n: int(''.join(n), 2), zip(*list(map(lambda n: BIN[int(n)], str(number)))))

if 0 <= y-dy < pow(2, d) and 0 <= x-dx < pow(2, d):
    move = list(map(lambda n: bin(n)[2:].zfill(d), [y-dy, x-dx]))
    answer = ''
    for index in range(d):
        answer += str(BIN.index(move[0][index] + move[1][index]))
    print(answer)
else:
    print(-1)