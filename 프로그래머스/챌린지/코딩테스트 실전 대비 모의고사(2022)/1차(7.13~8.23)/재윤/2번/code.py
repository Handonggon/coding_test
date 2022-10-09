def solution(want, number, discount):
    answer = 0
    dic ={}
    dic = dic.fromkeys(discount,0)
    count = 0
    for i in want:
        dic[i] = number[count]
        count +=1
    for i in range(len(discount)):
        dic2 = dic.copy() 
        f = 0
        if len(discount)-i >= 10:
            for j in discount[i:i+10]:
                dic2[j] -= 1
            for m in dic2:
                if dic2[m] > 0:
                    f += 1
                    break
                else:
                    pass
            if f == 1:
                continue
            else:
                answer += 1
    return answer