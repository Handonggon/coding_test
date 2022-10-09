def solution(s):
    if len(s) == 1 :
        return 1
    split_data = []
    for i in range(1,(len(s)//2)+1) :
        temp_list = []
        for j in range(0,len(s),i) :
            temp_list.append(s[j:j+i])
        split_data.append(temp_list)
    str_list = []
    for element in split_data :
        s = ''
        temp = 1
        for e in range(len(element)-1) :
            if element[e] == element[e+1] :
                temp += 1
            else :
                if temp == 1 :
                    s += element[e]
                else :
                    s += (str(temp)+element[e])
                temp = 1
        if temp == 1 :
            s += element[len(element)-1]
        else :
            s += (str(temp)+element[len(element)-1])
        str_list.append(s)
    for i in range(len(str_list)) :
        str_list[i] = len(str_list[i])
    
    return min(str_list)