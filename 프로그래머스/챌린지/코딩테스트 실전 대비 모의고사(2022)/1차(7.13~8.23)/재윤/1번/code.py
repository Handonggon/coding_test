def solution(x,y):
    answer = ''
    list_w = []
    dic= {}
    list_n = [i for i in range(10)]
    dicx = dic.fromkeys(list_n,0)
    dicy=dicx.copy()
    for i in x:
        dicx[int(i)] += 1
    for i in y:
        dicy[int(i)] += 1
    for i in range(10):
        if dicx[i] > 0 and dicy[i] > 0:
            count = min(dicx[i],dicy[i])
            for j in range(count):
                list_w.append(i)
        else:
            pass
    if len(list_w) == 0:
        return '-1'
    if list(set(list_w))==[0]:
        return "0"

    list_w.sort(reverse=True)
    for i in list_w:
        answer += str(i)
    return answer