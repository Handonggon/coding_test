def solution(priorities, location):
    list_p = sorted(set(priorities),reverse=True)
    k = 0
    list_result = []
    for i in list_p :
        while i in priorities :
            if priorities[0] == i :
                priorities[0] = 0
                list_result.append(k%len(priorities))
            priorities.append(priorities.pop(0))
            k += 1
    
    return list_result.index(location)+1