def solution(n):
    answer =''
    while n!=0:
        
        if n%3==0:
            if n!=3:
                n -=3
                answer += '4'
            else:
                answer += '4'
                break
            
        elif n%3==1:
            answer += "1"
            
        else:
            answer += "2"
            
        n = n//3
            
    return answer[::-1]
       