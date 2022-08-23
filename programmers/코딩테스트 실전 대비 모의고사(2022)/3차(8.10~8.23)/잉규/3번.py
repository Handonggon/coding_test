def solution(distance, scope, times):
    result_list = [distance]
    for point in range(len(scope)) :
        for i in range(min(scope[point])-1,max(scope[point])):
            if i  % (times[point][0]+times[point][1]) < times[point][0] :
                result_list.append(i+1)
    return min(result_list)