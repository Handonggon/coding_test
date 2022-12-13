from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))

# N = 7
# info = [0, 1, 2, 4, 6, 3, 10] # [0, 0, 10, 2, 4, 6, 2, 3, 1, 4, 1, 3, 6, 10]

answer = []
for permutation in map(list, permutations(info, N)):
    sequence = [-1] * (2 * N)
    index = 0
    while permutation and index < (2 * N):
        if sequence[index] == -1:
            number = permutation.pop()
            sequence[index] = number
            if index + number + 1 < (2 * N) and sequence[index + number + 1] == -1:
                sequence[index + number + 1] = number
            else:
                break
        index += 1

    if -1 not in sequence:
        answer.append(sequence)

print(*sorted(answer, key = lambda item: tuple([item[index] for index in range(N * 2)]))[0]) if answer else print(-1)