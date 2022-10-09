from itertools import combinations
import collections

def solution(orders, course):
    result = []
    for i in range(len(orders)) :
        orders[i] = sorted(orders[i])
    
    for i in course :
        for j in orders :
            if len(j) >= i :
                for p in combinations(j, i):
                    result.append(''.join(p))

    most_ordered = collections.Counter(result).most_common()
    answer = []
    for i in course :
        max = 0
        for j in most_ordered :
            if j[1] >= 2 and len(j[0]) == i:
                max = j[1]
                break
        for j in most_ordered :
            if max == j[1] and len(j[0]) == i:
                answer.append(j[0])
        
    return sorted(answer)