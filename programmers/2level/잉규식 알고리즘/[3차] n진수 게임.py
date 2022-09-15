def radix_Transformation(num, n) :
    dic_R = {10 : "A",11 : "B",12 : "C",13 : "D",14 : "E", 15 : "F"}
    temp = []
    while num >= n :
        if num % n in dic_R.keys() :
            temp.append(dic_R[num % n])
        else :
            temp.append(str(num % n))
        num //= n
    if num in dic_R.keys() :
        temp.append(dic_R[num])
    else :
        temp.append(str(num))
        
    return ''.join(temp[::-1])
    
def solution(n, t, m, p):
    order = ""
    for i in range(t*m) :
        order += radix_Transformation(i,n)
    result = ""
    for i in range(len(order)) :
        if i%m + 1 == p :
            result += order[i]
    
    return result[:t]