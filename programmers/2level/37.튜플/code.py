def solution(s):
    s = s[1:len(s)-1]
    list_n = []
    baguni = []
    string = ""
    dict = {}
    division = True
    for i in s:
        if i == "{":
            division = True
        elif i == "}":
            baguni.append(string)
            list_n.append(baguni)
            string = ''
            baguni = []
            division = False
        elif i.isdigit() == True:
            string += i
        else: #쉼표
            if division == True:
                baguni.append(string)
                string = ""
            else:
                pass
    list_n = sorted(list_n,key = lambda x : len(x))
    for i in list_n[-1]:
        dict[str(i)] = 0
    for i in list_n:
        for j in i:
            dict[j] += 1
    list_n = sorted(dict,key=lambda x : dict[x])
    answer = []
    while list_n != []:
        answer.append(int(list_n.pop()))
    return answer