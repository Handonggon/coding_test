import copy

def powerSet(list_X) :
    subsets = [[]]

    for num in list_X :
        size = len(subsets)
        for temp in range(size) :
            subsets.append(subsets[temp] + [num])
    return subsets

def solution(beginning, target):
    beginning_row = [i for i in range(len(beginning))]
    beginning_column = [i for i in range(len(beginning[0]))]
    order_list = []
    result_len = []
    for i in powerSet(beginning_row) :
        for j in powerSet(beginning_column) :
            order_list.append([i,j])

    
    for k in order_list :
        compare = copy.deepcopy(beginning)
        for i in range(len(beginning_row)) :
            for j in range(len(beginning_column)) :
                if i in k[0] and j in k[1] :
                    continue
                elif j in k[1] or i in k[0] :
                    if compare[i][j] == 0 :
                        compare[i][j] = 1
                    else :
                        compare[i][j] = 0
      
        if target == compare :
            result_len.append(len(k[0])+len(k[1]))
    
    if result_len == [] :
        return -1
    else :
        return min(result_len)