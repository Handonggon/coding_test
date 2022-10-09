def perm(list_X,n) :
    result = []
    if n > len(list_X) :
        return result
    if n == 1 :
        for i in list_X :
            result.append([i])
    elif n > 1 :
        for i in range(len(list_X)) :
            temp = [i for i in list_X]
            temp.remove(list_X[i])
            for p in perm(temp,n-1) :
                result.append([list_X[i]]+p)

    return result

def solution(k, dungeons):
    dungeons = perm(dungeons,len(dungeons))
    result = []
    for i in dungeons :
        count = 0
        piro = k
        for j in i :
            if j[0] <= piro and j[1] <= piro :
                count += 1
                piro -= j[1]
        result.append(count)
    
    return max(result)
