def solution(land):
    maxt = [0,0]
    temp = -1
    temp_list = [0,0,0,0]
    for arr in land :
        for idx in range(len(arr)) :
            if idx == temp :
                temp_list[idx] = maxt[1] + arr[idx]
            else :
                temp_list[idx] = maxt[0] + arr[idx]
        temp = temp_list.index(max(temp_list))
        sort_temp = sorted(temp_list)
        maxt = [sort_temp[-1],sort_temp[-2]]
        
    return max(temp_list)