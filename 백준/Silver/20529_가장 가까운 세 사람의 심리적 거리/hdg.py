import sys
import itertools

TYPE = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
score = [[[0 for k in range(len(TYPE))] for j in range(len(TYPE))] for i in range(len(TYPE))]
for i in range(len(TYPE)):
    for j in range(len(TYPE)):
        for k in range(len(TYPE)):
            score[i][j][k] += len(set(list(TYPE[i]) + list(TYPE[j]))) - 4
            score[i][j][k] += len(set(list(TYPE[i]) + list(TYPE[k]))) - 4
            score[i][j][k] += len(set(list(TYPE[j]) + list(TYPE[k]))) - 4


T = int(input())
for t in range(T):
    N = int(input())
    info = input().split(' ')
    if N > 32:
        print(0)
    else:
        answer = 8 + 1
        for i in range(len(info)):
            for j in range(len(info)):
                for k in range(len(info)):
                    if i == j or j == k or i == k:
                        continue
                    answer = min(answer, score[TYPE.index(info[i])][TYPE.index(info[j])][TYPE.index(info[k])])
        print(0 if answer > 8 else answer)