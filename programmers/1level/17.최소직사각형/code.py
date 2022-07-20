def solution(sizes):
    w=[]
    h=[]
    for i in sizes:
        a,b = i
        if a < b:
            a,b = b,a
        else:
            pass
        w.append(a)
        h.append(b)
        
        
    
    return max(w)*max(h)