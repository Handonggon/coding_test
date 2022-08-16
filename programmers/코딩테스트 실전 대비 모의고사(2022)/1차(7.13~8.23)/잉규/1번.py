def solution(X, Y):
    dic_result = {i : [0,0] for i in range(9,-1,-1)}
    result = ""
    for i in X :
        dic_result[int(i)][0] += 1
    for i in Y :
        dic_result[int(i)][1] += 1
    for i in dic_result.keys() :
        if sum(dic_result[i]) >= 2 :
            result += str(i) * min(dic_result[i])
    if result == "" :
        return "-1"
    elif result[0] == "0" and result[1] == "0" :
        return "0"
    else :
        return result










