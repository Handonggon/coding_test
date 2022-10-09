from itertools import *
def solution(clothes):
    answer = 0
    closet = {}
    for i in clothes:
        closet[i[1]] = []
    for i in clothes:
        closet[i[1]].append(i[0])
    for i in closet:
        closet[i] = len(closet[i])

    count = len(closet)
    if count == 30:
        a = count
        while count!=0:
            c = 1
            while a != 0:
                c *= a
                a -= 1
            answer += c 
            count -= 1
        return answer
    while count != 0:
        list_n = []
        a = list(combinations(closet,count))
        for i in a:
            m = []
            for j in i:
                m.append(closet[j])
            list_n.append(m)
        for i in list_n:
            s = 1
            for j in i:
                s *= j
            answer += s
        count -= 1
    return answer