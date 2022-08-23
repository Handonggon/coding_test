def solution(s):
    a = [s[0]]
    
    for i in s[1::]:
        if a != []:
            if i == a[-1]:
                a.pop()
            else: a.append(i)
        else: a.append(i)
    
    if a==[]: return 1
    else: return 0