def solution(s):
    answer = [0,0]
    
    while s != "1" :
        temp = ''
        count = 0
        for i in s :
            if i == "1" :
                temp += i
            else :
                count += 1
        answer[0] += 1
        answer[1] += count
        s = bin(len(temp))[2:]
        
    return answer