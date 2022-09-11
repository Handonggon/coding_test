import math

def solution(fees, records):
    res = []
    
    a, c = {}, {}
    for i in records:
        b = i.split(" ")
        if b[1] not in a:
            a[b[1]] = b[0]
        else:
            f = a.get(b[1]).split(":")
            ff = int(f[0]) * 60 + int(f[1])
            s = b[0].split(":")
            ss = int(s[0]) * 60 + int(s[1])
            del a[b[1]]
            if b[1] not in c:
                c[b[1]] = ss - ff
            else:
                c[b[1]] += (ss - ff)
    while a:            
        if list(a.keys())[0] in c:
            list_f = list(a.keys())
            f = a.get(list_f[0]).split(":")
            ff = int(f[0]) * 60 + int(f[1])
            c[list_f[0]] += (1439 - ff)
            del a[list_f[0]]
            list_f.remove(list_f[0])
        else:
            list_f = list(a.keys())
            f = a.get(list_f[0]).split(":")
            ff = int(f[0]) * 60 + int(f[1])
            c[list_f[0]] = (1439 - ff)
            del a[list_f[0]]
            list_f.remove(list_f[0])
    
    d = sorted(c.items())
    
    res = []
    
    for i in d:
        value = i[1]
        print(value)
        if value > fees[0]:
            res.append(math.ceil((value - fees[0]) / fees[2]) * fees[3] + fees[1])
        else:
            res.append(fees[1])
            
    return res