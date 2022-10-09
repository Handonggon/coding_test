def powerSet(list_X) :
    subsets = [[]]

    for num in list_X :
        size = len(subsets)
        for temp in range(size) :
            subsets.append(subsets[temp] + [num])
    return subsets

def solution(number):
    p=powerSet(number)
    result = []

    for i in p :
        if len(i) == 3 and sum(i) == 0 :
            result.append(i)
    return len(result)