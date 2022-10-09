def solution(brown, yellow):
    divisor = []
    for i in range(yellow,0,-1) :
        if yellow %i == 0 :
            divisor.append(i)
            
    if divisor == [1]:
        return [3,3]
    else :
        inc = 0
        if len(divisor)%2 == 0 :
            idx = len(divisor)//2
            while True :
                if (divisor[idx-1-inc]+2)*(divisor[idx+inc]+2) - yellow == brown :
                    return [divisor[idx-1-inc]+2,divisor[idx+inc]+2]
                else :
                    inc += 1
        else :
            idx = len(divisor)//2
            while True :
                if (divisor[idx-inc]+2)*(divisor[idx+inc]+2) - yellow == brown :
                    return [divisor[idx-inc]+2,divisor[idx+inc]+2]
                else :
                    inc += 1