def solution(files):
    dict = {}
    list_w = []
    answer = []

    for i in files:
        for m in range(len(i)):
            if i[m].isdigit() == True:
                a = m
                break
        nt = i[a:]
        b = "space"
        for j in range(len(nt)):
            if nt[j].isdigit() == False:
                b = j
                break
        head = i[:a]
        dict[head.lower()] = []
        n = ""
        t = ""
        if b != "space":
            n += nt[:j]
            t += nt[j:]
        else:
            n += nt
        list_w.append([head,n,t])
    for i in list_w:
        dict[i[0].lower()].append(i)
    for i in dict:
        dict[i].sort(key=lambda x : int(x[1]))
    for i in sorted(dict,key=lambda x : dict[x]):
        for j in dict[i]:
            string = ""
            string += j[0]
            string += j[1]
            string += j[2]
            answer.append(string)
    return answer