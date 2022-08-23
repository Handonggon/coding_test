from itertools import combinations

def solution(number):
    
    a = list(combinations(number, 3))
    res = 0
    for i in a:
        if sum(i) == 0:
            res += 1

    return res