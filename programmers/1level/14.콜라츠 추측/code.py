def solution(num):
    list_n = []
    list_n.append(num)
    for i in list_n:
        if len(list_n) == 501::
            if list_n[-1] == 1:
                return 500
                break
            else:
                return -1
                break
        else:
            if i == 1:
                break
            else:
                if i % 2 == 0:
                    list_n.append(int(i/2))
                else:
                    list_n.append(i*3+1)
    return len(list_n)-1