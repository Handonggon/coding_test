def solution(n, words):
    answer = [0,0]
    dict ={}
    for i in words:
        dict[i] = 0
    list_n = [i for i in range(1,n+1)]
    list_w =[]
    count = -1
    words.reverse()
    while words != []:
        count += 1
        a =words.pop()
        if len(list_w) > 0 :
            if list_w[-1][-1] == a[0] and dict[a] == 0:
                list_w.append(a)
            else:
                words.append(a)
                break
        else :
            list_w.append(a)
        dict[a] += 1
    if len(words) == 0:
        return[0,0]
    else :
        answer[0] += list_n[count%n]
        answer[1] += (count//n)+1

    return answer