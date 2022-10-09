def powerSet(list_X) :
    subsets = [[]]

    for num in list_X :
        size = len(subsets)
        for temp in range(size) :
            subsets.append(subsets[temp] + [num])
    return subsets

def solution(numbers, target):
    result = 0
    cases = powerSet([i for i in range(0,len(numbers))])
    for case in cases :
        temp = numbers[:]
        for idx in range(0,len(temp)) :
            if idx in case :
                temp[idx] *= -1
        if sum(temp) == target :
            result +=1
    
    return result