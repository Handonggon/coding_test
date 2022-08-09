def solution(progresses, speeds):
    a = []
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i] == 0:
            a.append((100 - progresses[i]) // speeds[i])
        else:
            a.append((100 - progresses[i]) // speeds[i] + 1)
    c=[]
    while True:
        b = []
        d = a[0]
        for i in a:
            if d >= i:
                b.append(i)    
            else:break
        for i in b:
            a.remove(i)
        c.append(len(b))
        if a == []:
            break
    
    return c