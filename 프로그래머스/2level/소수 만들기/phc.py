def prime(n):
    if n == 1:return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    res = ''
    while True:
        res = str(n % k) + res
        n //= k
        if n == 0: break
    
    cnt, n = 0 ,0
    
    while n < len(res):
        check = ''
        while True:
            if n == len(res): break
            elif res[n] == '0': 
                n+=1
                break
            else: 
                check += res[n]
                n+=1
        if check == '': continue
        if prime(int(check)): cnt += 1
        
    return cnt