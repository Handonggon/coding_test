def solution(s):
    res = []
    i = 1
    
    while True:
        box = []
        if s[i] == "{":
            j = i+1
            while True:
                if s[i] == ',':
                    box.append(int(s[j:i]))
                    j = i+1
                elif s[i] == "}":
                    box.append(int(s[j:i]))
                    break
                i += 1
        if box != []: res.append(box)
        if i + 1 == len(s): break
        i += 1
    
    i, j = 0, 1
    ans = []
    while True:
        if len(res[i]) == j:
            for k in res[i]:
                if k not in ans: ans.append(k)
            i = 0
            j += 1
        else:
            i += 1
        if i == len(res): break
        
    return ans