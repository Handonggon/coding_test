import math
def solution(n, m):
    if n > m:
        n,m = m,n
    else :
        pass
    cf = []
    lcm = []
    if m % n == 0:
    else:
        if n % 2 == 0: #n이 짝수일 경우
            for i in range(1,int(n/2)+1):
                if n%i ==0:
                    if m%i == 0:
                        cf.append(i)
                    else:
                        pass
                else:
                    pass
        else: #n이 홀수일 경우
            for i in range(1,math.floor(n/2)+1):
                if n%i ==0:
                    if m%i == 0:
                        cf.append(i)
                else:
                    pass
                
    for i in range(0,n*m+1,m):
        if i ==0:
             continue  
        if i%n == 0:
            lcm.append(i)
        else :
            pass
            
    return [cf[-1],lcm[0]]