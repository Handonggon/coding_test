def solution(record):
    ans = []
    split_i = [i.split(" ") for i in record]
    stacks_id = [i[1] for i in split_i if i[0] != "Change"]
    stacks_ent = [i[0] for i in split_i if i[0] != "Change"]

    id = {}
    for i in split_i:
        if len(i) == 3:
            id[i[1]] = i[2]
                
    for i in range(len(stacks_ent)):
        if stacks_ent[i] == 'Enter':
            ans.append(id.get(stacks_id[i]) + "님이 들어왔습니다.")
        else: ans.append(id.get(stacks_id[i]) + "님이 나갔습니다.")
    
    return ans