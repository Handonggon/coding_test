def solution(k, d):  
    import itertools
    k_k = k
    a = itertools.permutations(d, len(d))
    b = []    
    for i in a:
        res = 0
        k = k_k
        for j in range(len(i)):
            if k >= i[j][0]:
                k = k - i[j][1]
                res += 1               
        b.append(res)
    return max(b)       