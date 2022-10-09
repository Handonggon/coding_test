from itertools import *
def solution(k, dungeons):
    answer = 0
    list_n = list(permutations(dungeons, len(dungeons)))
    for i in list_n:
        a = k
        count = 0
        for j in i:
            if a >= j[0]:
                a -= j[1]
                count += 1
            else:
                break
        if answer < count:
                answer = count
        else:
            pass
    return answer