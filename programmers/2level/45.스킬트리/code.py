def solution(skill, skill_trees):
    answer = 0
    list_s = []
    for i in skill:
        list_s.append(i)
    for i in skill_trees:
        a = list_s.copy()
        b = True
        for j in i:
            if len(a) == 1:
                break
            search = a[1:]
            if j != a[0]:
                if j in search:
                    b = False
                    break
                else:
                    pass
            else:
                a.pop(0)
        if b == True:
            answer += 1
        else:
            pass
        
    
    return answer