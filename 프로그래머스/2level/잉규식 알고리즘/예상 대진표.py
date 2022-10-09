def Prime_number(n) :
    if n% 2 == 0 :
        return n
    else :
        return n+1

def solution(n,a,b):
    answer = 0
    
    while a+1 != b and b+1 != a :
        a = Prime_number(a)//2
        b = Prime_number(b)//2
        answer += 1
    if min(a,b) % 2 == 0 :
        temp = min(a,b)
        if temp%4 != 0 :
            answer -= 2
        while temp != 0 :
            temp //= 2
            answer += 1
        return answer 
    else :
        return answer + 1