def solution(cache, citi):
    a = []
    res = 0
    
    if cache == 0: return len(citi) * 5
    else:
        for i in citi:
            
            if i.lower() in a: 
                res += 1
                a.remove(i.lower())
            else: res += 5
            a.insert(0, i.lower())

            if len(a) > cache:
                a.pop()
                
    return res