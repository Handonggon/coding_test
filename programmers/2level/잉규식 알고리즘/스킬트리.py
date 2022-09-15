def solution(skill, skill_trees):
    result = 0
    skill_order = list(skill)
    list_skill =[[],skill_order]
    for i in range(1,len(skill_order)) :
        list_skill.append(skill_order[:-i])
    for s in skill_trees :
        stack = []
        for k in s :
            if k in skill_order :
                stack.append(k)
        if stack in list_skill :
            result += 1
    
    return result