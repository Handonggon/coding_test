def solution(new_id):
    new_id_list = list(new_id)
    id_2 = ""
    for i in range(len(new_id_list)):
        if new_id_list[i].isalpha():
            new_id_list[i] = new_id_list[i].lower()
    for i in range(len(new_id_list)):
        if new_id_list[i].isalpha() or new_id_list[i].isdigit() or new_id_list[i] == '-' or new_id_list[i] == '_' or new_id_list[i] == "." :
            id_2 += new_id_list[i]
        else:
            pass
    id_2_list = list(id_2)
    id_3 = []
    for i in range(len(id_2_list)):
        if i == 0:
            id_3.append(id_2_list[i])
        else:
            if id_2_list[i] == ".":
                if id_3[-1] == ".":
                    pass
                else:
                    id_3.append(id_2_list[i])
            else:
                id_3.append(id_2_list[i])
    while len(id_3)>0 and id_3[0]=='.':
        id_3.pop(0)
    if len(id_3) == 0:
        id_3 = ["a"]
    while id_3[-1]==".":
        id_3.pop(-1)
    id_4 = id_3
    if id_4 == []:
        id_4 = ['a']
    id_5 = id_4
    if len(id_5) > 15 :
        id_5 =id_5[:15]
        while id_5[-1] == ".":
            id_5.pop(-1)
    id_6 = id_5
    while len(id_6) <= 2:
        id_6.append(id_6[-1])
    id_7 = id_6
    answer = ""
    for i in id_7:
        answer += i

    return answer