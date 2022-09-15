def solution(dirs):
    position = [0,0]
    move_list = []
    for i in dirs :
        movepoint = position[:]
        if i == "U" :
            movepoint[1] += 1
            if movepoint[1] > 5 :
                movepoint[1] -= 1
                continue
        elif i == "L" :
            movepoint[0] -= 1
            if movepoint[0] < -5 :
                movepoint[1] += 1
                continue
        elif i == "R" :
            movepoint[0] += 1
            if movepoint[0] > 5 :
                movepoint[0] -= 1
                continue
        else :
            movepoint[1] -= 1
            if movepoint[1] < -5 :
                movepoint[1] += 1
                continue
        move_list.append([position,movepoint])
        position = movepoint
        
    reverse_list = []
    result = []
    for i in move_list :
        reverse_list.append([i[1],i[0]])
    move_list += reverse_list
    for i in move_list :
        if i not in result :
            result.append(i)
    
    return len(result)//2
    

