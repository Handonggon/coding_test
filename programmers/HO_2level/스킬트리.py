def solution(a,b):
    res = 0
    
    for i in b:
        cnt = 0
        for j in i:
            if j not in a:
                continue
            elif j == a[cnt]:
                cnt += 1
            elif j in a and j != a[cnt]:
                res -= 1
                break
        res += 1        
                
    return res                      