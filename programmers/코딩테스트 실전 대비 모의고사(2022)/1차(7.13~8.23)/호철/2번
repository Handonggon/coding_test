def solution(want, number, discount):
    
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    res = 0
    for i in range(len(discount) - sum(number) + 1):
        dic_2 = {}
        for j in range(sum(number)):
            if discount[i + j] not in dic_2:
                dic_2[discount[i + j]] = 1
            else: dic_2[discount[i + j]] += 1

        if dic == dic_2:
            res += 1

    return res
