def solution(topping):
    answer = 0
    dic = {}
    dic2 = set()
    list_n = [i for i in topping]
    list_n = list(set(list_n))
    dic = dic.fromkeys(list_n,0)    
    for i in topping:
        dic[i] += 1
    for i in topping:
        dic2.add(i)
        dic[i] -= 1
        if dic[i] == 0:
            del dic[i]

        if len(dic2) == len(dic):
            answer += 1
        else:
            pass
    return answer