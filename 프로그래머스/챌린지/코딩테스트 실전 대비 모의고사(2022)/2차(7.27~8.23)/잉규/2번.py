def solution(topping):
    dic_topping = {}
    set_topping = set()
    count = 0
    for i in topping :
        if i not in dic_topping.keys() :
            dic_topping[i] = 1
        else :
            dic_topping[i] += 1
    
    for i in topping :
        set_topping.add(i)
        dic_topping[i] -= 1
        if dic_topping[i] == 0 :
            dic_topping.pop(i)
        if len(set_topping) == len(dic_topping) :
            count += 1
    
    return count
