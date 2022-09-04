from itertools import combinations
def solution(number):
    answer = 0
    number.sort()
    list_n = list(combinations(number, 3))
    for i in list_n:
        if sum(i) == 0:
            answer += 1
        else:
            pass
    return answer