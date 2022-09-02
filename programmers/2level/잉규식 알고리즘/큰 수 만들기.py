def solution(number, k):
    number_list = []
    for i in number :
        number_list.append(int(i))
    result = ''
    max_num = [0,0]
    k = len(number) - k
    while k>0 :
        for m in range(max_num[1],len(number_list)-k+1) :
            if number_list[m] == 9 :
                max_num = [number_list[m],m+1]
                break
            elif number_list[m] > max_num[0] :
                max_num = [number_list[m],m+1]
        result += str(max_num[0])
        max_num[0] = 0
        k -= 1
    
    return result